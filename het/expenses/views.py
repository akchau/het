from core import views as core_views
from .forms import ExpenseForm, ExpenseEditForm
from .models import Expense
from django.contrib.auth.decorators import login_required

PAGE = "expenses/pages/expenses.html"
MODEL = Expense
FORM = ExpenseForm
EDIT_FORM = ExpenseEditForm


@login_required
def list(request):
    """
    Список с формой доабвления новой записи.
    """
    edit_mode_value = request.GET.get('edit_mode', None)
    edit_mode = True if edit_mode_value == 'True' else None
    edit_pk = None
    if edit_mode:
        edit_pk_value = request.GET.get('edit_pk', '')
        try:
            edit_pk = int(edit_pk_value)
        except ValueError:
            edit_pk = None
    context = {
        "verbose_title": "Мои расходы",
        "verbose_action": "Добавьте расход",
        "num_record_in_page": 14,
        "order_by": "-pub_date",
        "edit_mode": edit_mode,
        "edit_pk": edit_pk,
    }

    return core_views.listing_with_creating(
        request=request,
        template=PAGE,
        model=MODEL,
        form_class=FORM,
        context=context,
        edit_form_class=EDIT_FORM
    )


@login_required
def new(request):
    """
    Создание записи.
    """
    return core_views.add_with_set_user(
        request=request,
        form_class=FORM
    )


@login_required
def delete(request, pk):
    """
    Удаление записи.
    """
    return core_views.detete_obj(
        request=request,
        pk=pk,
        model=MODEL,
        redirect_name=FORM.Meta.redirect_name
    )


@login_required
def edit(request, pk: int):
    return core_views.edit_obj(request=request, pk=pk, form_class=EDIT_FORM)
