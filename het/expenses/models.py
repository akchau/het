from django.db import models
from django.contrib.auth import get_user_model

from core.models import TransactionItemModel
from expenses.categories.models import ExpenseCategory

User = get_user_model()

class Expense(TransactionItemModel):
    """
    Модель расхода.
    """
    category = models.ForeignKey(
        ExpenseCategory,
        on_delete=models.SET_NULL,
        related_name="expenses",
        verbose_name="Категория",
        null=True,
        blank=True,
        help_text="Выберите категорию из списка."
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="expenses",
        verbose_name="Пользователь",
    )

    class Meta:
        verbose_name = "Расход"
        verbose_name_plural = "Расходы"

    def __str__(self):
        return f'{self.category} - {self.sum_of_expense}[{self.currency}]'