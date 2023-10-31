from core import views as core_views
from .forms import ExpenseForm
from .models import Expense
from django.contrib.auth.decorators import login_required

PAGE = "expenses/pages/expenses.html"
MODEL = Expense
FORM = ExpenseForm


@login_required
def list(request):
    """
    Список с формой доабвления новой записи.
    """

    context = {
        "verbose_title": "Мои расходы",
        "verbose_action": "Добавьте расход",
        "num_record_in_page": 14,
        "order_by": "-pub_date",
    }

    return core_views.listing_with_creating(
        request=request,
        template=PAGE,
        model=MODEL,
        form_class=FORM,
        context=context
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
