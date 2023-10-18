from .models import Expense, ExpenseCategory
from django import forms


class ExpenseForm(forms.ModelForm):
    """Форма для создания и редактирования траты"""
    class Meta:
        model = Expense
        fields = (
            "category",
            "currency",
            "sum_of_expense",
            "comment",
        )
        redirect_name = "expenses:list"
