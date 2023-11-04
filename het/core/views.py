from django import forms
from django.db import models
from django.shortcuts import get_object_or_404, redirect, render
from core.pagination import get_page_obj


def listing_with_creating(request, template: str,
                          model: models.Model, form_class: forms.ModelForm,
                          context: dict, edit_form_class: forms.ModelForm):
    """
    Базовая вью-функция для отображения сущности с
    формой добавления и пагинатором
    """
    records = model.objects.filter(
        user=request.user.pk).order_by(context["order_by"])
    # Пагинация спсика
    page_obj = get_page_obj(
        request,
        records,
        context["num_record_in_page"]
    )

    # kwargs = {'user': request.user}
    # Форма добавления новой записи
    new_form = form_class(
        None,
        files=request.FILES or None,
        user=request.user
    )

    edit_form = None
    if context["edit_mode"]:
        edit_model = edit_form_class.Meta.model
        object_instance = get_object_or_404(edit_model, pk=context["edit_pk"])
        edit_form = edit_form_class(
            request.POST or None,
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
        "edit_form": edit_form
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


def edit_obj(request, form_class: forms.ModelForm):
    form = form_class(
        request.POST,
        user=request.user
    )
    if form.is_valid():
        new_object = form.save(commit=False)
        new_object.user = request.user
        form.save(commit=True)
        form.save()
        return redirect(form_class.Meta.redirect_name)
    raise ValueError('Невалидная форма')
