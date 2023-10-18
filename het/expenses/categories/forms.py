from .models import ExpenseCategory
from django import forms


class ExpenseCategoryForm(forms.ModelForm):
    """Форма для создания категории расхода."""
    class Meta:
        model = ExpenseCategory
        fields = (
            "name",
        )
        redirect_name = "expenses_categories:list"


class ExpenseCategoryFilter(forms.Form):
    pass