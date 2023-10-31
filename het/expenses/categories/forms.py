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

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ExpenseCategoryForm, self).__init__(*args, **kwargs)


class ExpenseCategoryFilter(forms.Form):
    pass