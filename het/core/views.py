from urllib.parse import urlencode
from django import forms
from django.db import models
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from core.pagination import get_page_obj
from expenses.models import Expense
from expenses.categories.models import ExpenseCategory


def listing_with_creating(request, template: str,
                          model: models.Model, form_class: forms.ModelForm,
                          context: dict, edit_form_class: forms.ModelForm,
                          category_filter_form_class: forms.ModelForm):
    """
    Базовая вью-функция для отображения сущности с
    формой добавления и пагинатором
    """
    my_balance = Expense.objects.filter(user=request.user).aggregate(Sum('sum_of_expense'))['sum_of_expense__sum']
    if my_balance is None:
        my_balance = 0
    if context["filter_category"] is not None:
        print(context["filter_category"])
        records = model.objects.filter(
            user=request.user.pk,
            category=context["filter_category"]
        ).order_by(context["order_by"])
    else:
        print(context["filter_category"])
        records = model.objects.filter(
            user=request.user.pk,
        ).order_by(context["order_by"])
    # Пагинация спсика
    page_obj = get_page_obj(
        request,
        records,
        context["num_record_in_page"]
    )
    category_filter_form = None
    if category_filter_form_class is not None:
        category_filter_form = category_filter_form_class(
            None,
            user=request.user
        )
    new_form = form_class(
        None,
        user=request.user
    )
    edit_form = None
    if context["edit_mode"]:
        edit_model = edit_form_class.Meta.model
        object_instance = get_object_or_404(edit_model, pk=context["edit_pk"])
        edit_form = edit_form_class(
            None,
            user=request.user,
            instance=object_instance,
        )

    context = {
        "title": context["verbose_title"],
        "header": context["verbose_title"],
        "page_obj": page_obj,
        "form": new_form,
        "action": context["verbose_action"],
        "edit_mode": context["edit_mode"],
        "edit_pk": context["edit_pk"],
        "edit_form": edit_form,
        "category_filter_form": category_filter_form,
        "my_balance": my_balance
    }
    return render(request, template, context)


def add_with_set_user(request, form_class: forms.ModelForm):
    """Создание сущности."""
    form = form_class(request.POST, user=request.user)
    if form.is_valid():
        new_object = form.save(commit=False)
        new_object.user = request.user
        form.save(commit=True)
        return redirect(form_class.Meta.redirect_name)
    raise ValueError('Невалидная форма')


def detete_obj(request, pk, model, redirect_name):
    if model.objects.filter(pk=pk, user=request.user.pk).exists():
        model.objects.filter(pk=pk, user=request.user.pk).delete()
    return redirect(redirect_name)


def edit_obj(request, pk: int, form_class: forms.ModelForm):
    edit_model = form_class.Meta.model
    object_instance = get_object_or_404(edit_model, pk=pk)
    form = form_class(
        request.POST,
        user=request.user,
        instance=object_instance,
    )
    if form.is_valid():
        new_object = form.save(commit=False)
        new_object.user = request.user
        form.save(commit=True)
    return redirect(form_class.Meta.redirect_name)


def filter_category_redirect(request, form_class: forms.ModelForm):
    form = form_class(
        request.POST,
        user=request.user,
    )
    if form.is_valid():
        new_object = form.save(commit=False)
        category = new_object.category
        print(category)
        object = ExpenseCategory.objects.get(name=category)
        base_url = reverse(form_class.Meta.redirect_name)
        query_string = urlencode({'filter_category': object.pk})
        url = '{}?{}'.format(base_url, query_string)
        print(url)
    return redirect(url)
