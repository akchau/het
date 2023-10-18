from django.db import models
from django.contrib.auth import get_user_model

from core.models import ItemModel

User = get_user_model()

class ExpenseCategory(ItemModel):
    """
    Модель категории.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="expenses_categories",
        verbose_name="Пользователь",
    )

    class Meta:
        verbose_name = "Категория расходов"
        verbose_name_plural = "Категори расходов"