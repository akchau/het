from core import views as core_views
from .forms import ExpenseForm
from .models import Expense
from het.settings import (
    DEFAULT_PAGINATION_EXPENSES,
)

REDIRECT_NAME = "expenses:expenses"

def list(request):
    """
    Список расходов.
    """
    return core_views.listing_with_creating(
        request=request,
        template="expenses/expenses_list.html",
        model=Expense,
        default_pagination_num=DEFAULT_PAGINATION_EXPENSES,
        form_class=ExpenseForm,
        title="Мои расходы.",
        order_by="-pub_date"
    )

def new(request):
    """
    Создание расхода.
    """
    return core_views.add_with_set_user(
        request=request,
        form_class=ExpenseForm,
        redirect_name=REDIRECT_NAME
    )

def delete(request, pk):
    """
    Удаление расхода.
    """
    return core_views.detete_obj(
        request=request,
        pk=pk,
        model=Expense,
        redirect_name=REDIRECT_NAME
    )
