from django.db import models
from django.contrib.auth import get_user_model
from core.models import CURRENCY

User = get_user_model()

class ExpenseCategory(models.Model):
    """
    Модель категории.
    """
    name = models.CharField(
        "Название категории расхода",
        max_length=200,
        help_text="Укажите название категории расхода",
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="categories_expense",
        verbose_name="Пользователь",
    )

    class Meta:
        verbose_name = "Категория расхода"
        verbose_name_plural = "Категори расхода"
        unique_together = ("user", "name")

    def __str__(self):
        return self.name

class Expense(models.Model):
    """
    Модель расхода.
    """
    category = models.ForeignKey(
        ExpenseCategory,
        on_delete=models.SET_NULL,
        related_name="expenses",
        verbose_name="Категория",
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="expenses",
        verbose_name="Пользователь",

    )
    currency = models.CharField(
        "Валюта",
        choices=CURRENCY,
        max_length=5,
        default=CURRENCY[0][0]
    )

    sum_of_expense = models.PositiveIntegerField("Сумма")

    pub_date = models.DateTimeField(
        "Время занесения",
        auto_now_add=True,
    )

    comment = models.TextField(
        "Комментарий",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Расход"
        verbose_name_plural = "Расходы"

    def __str__(self):
        return f'{self.category} - {self.sum_of_expense}[{self.currency}]'