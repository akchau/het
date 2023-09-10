from django.shortcuts import redirect, render
from core.pagination import get_page_obj


def listing_with_creating(request, template, model, default_pagination_num, form_class, title, order_by):
    """
    Базовая вью-функция для отображения сущности с формой добавления и пагинатором
    """
    records = model.objects.filter(user=request.user.pk).order_by(order_by)
    page_obj = get_page_obj(
        request,
        records,
        default_pagination_num
    )
    new_form = form_class(
        request.POST or None,
        files=request.FILES or None,
    )
    context = {
        "title": title,
        "header": title,
        "page_obj": page_obj,
        "form": new_form,
    }
    return render(request, template, context)


def add_with_set_user(request, form_class, redirect_name):
    """Создание сущности."""
    form = form_class(
        request.POST or None,
    )
    if form.is_valid():
        new_object = form.save(commit=False)
        new_object.user = request.user
        form.save(commit=True)
        return redirect(redirect_name)
    raise ValueError('Невалидная форма')


def detete_obj(request, pk, model, redirect_name):
    if model.objects.filter(pk=pk, user=request.user.pk).exists():
        model.objects.filter(pk=pk, user=request.user.pk).delete()
    return redirect(redirect_name)