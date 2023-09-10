from core import views as core_views
from .forms import ExpenseCategoryForm
from .models import ExpenseCategory
from het.settings import (
    DEFAULT_PAGINATION_EXPENSES_CATEGORIES
)

def list(request):
    """
    Список категорий.
    """
    return core_views.listing_with_creating(
        request=request,
        template="expenses/categories.html",
        model=ExpenseCategory,
        default_pagination_num=DEFAULT_PAGINATION_EXPENSES_CATEGORIES,
        form_class=ExpenseCategoryForm,
        title="Мои категории расходов.",
        order_by="name"
    )

def new(request):
    """
    Создание категории.
    """
    return core_views.add_with_set_user(
        request=request,
        form_class=ExpenseCategoryForm,
        redirect_name="expenses:categories"
    )

def delete(request, pk):
    """
    Удаление категории.
    """
    return core_views.detete_obj(
        request=request,
        pk=pk,
        model=ExpenseCategory,
        redirect_name="expenses:categories"
    )
