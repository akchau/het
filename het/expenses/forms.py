from django.utils import timezone
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
            "pub_date",
        )
        redirect_name = "expenses:list"

    def __init__(self, *args, **kwargs):
        self.user = kwargs.get('user')
        if self.user:
            kwargs.pop("user")
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = ExpenseCategory.objects.filter(
            user=self.user)
        if not self.instance.pk:
            self.initial['pub_date'] = timezone.now()


class ExpenseEditForm(forms.ModelForm):
    """Форма для создания и редактирования траты"""
    class Meta:
        model = Expense
        fields = (
            "category",
            "sum_of_expense",
            "pub_date",
        )
        redirect_name = "expenses:list"

    def __init__(self, *args, **kwargs):
        self.user = kwargs.get('user')
        if self.user:
            kwargs.pop("user")
        super(ExpenseEditForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = ExpenseCategory.objects.filter(
            user=self.user)


class CategoryFilterForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = (
            "category",
        )
        redirect_name = "expenses:list"
        filter_model = ExpenseCategory

    def __init__(self, *args, **kwargs):
        self.user = kwargs.get('user')
        if self.user:
            kwargs.pop("user")
        super(CategoryFilterForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = ExpenseCategory.objects.filter(
            user=self.user)
