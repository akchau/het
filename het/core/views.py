from django.shortcuts import redirect, render
from core.pagination import get_page_obj


def listing_with_creating(request, template, model, form_class, context):
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
    # Форма добавления новой записи
    new_form = form_class(
        request.POST or None,
        files=request.FILES or None,
    )
    context = {
        "username": request.user.username,
        "user_pk": request.user.pk,
        "title": context["verbose_title"],
        "header": context["verbose_title"],
        "page_obj": page_obj,
        "form": new_form,
        "action": context["verbose_action"]
    }
    return render(request, template, context)


def add_with_set_user(request, form_class):
    """Создание сущности."""
    form = form_class(request.POST)
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
