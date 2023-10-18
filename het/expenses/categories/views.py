from core import views as core_views
from .forms import ExpenseCategoryForm
from .models import ExpenseCategory


PAGE = "expenses/pages/categories.html"
MODEL = ExpenseCategory
FORM = ExpenseCategoryForm


def list(request):
    """
    Список категорий.
    """
    context = {
        "verbose_title": "Мои категории расходов",
        "verbose_action": "Добавьте категорию расходов",
        "num_record_in_page": 5,
        "order_by": "name",
    }

    return core_views.listing_with_creating(
        request=request,
        context=context,
        template=PAGE,
        model=MODEL,
        form_class=FORM
    )


def new(request):
    """
    Создание категории.
    """
    return core_views.add_with_set_user(
        request=request,
        form_class=FORM
    )


def delete(request, pk):
    """
    Удаление категории.
    """
    return core_views.detete_obj(
        request=request,
        pk=pk,
        model=MODEL,
        redirect_name=FORM.Meta.redirect_name
    )
