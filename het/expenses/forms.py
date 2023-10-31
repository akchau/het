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

    def __init__(self, *args, **kwargs):
        self.user = kwargs.get('user')
        if self.user:
            kwargs.pop("user")
        print(self.user) # эту строку можно заменить на `user = kwargs.get('user')`, если user не всегда передается в kwargs
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = ExpenseCategory.objects.filter(user=self.user)
