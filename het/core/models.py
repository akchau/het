from django.utils import timezone
from django.db import models

CURRENCY = [
    ("RUB", "RUB")
]


class ItemModel(models.Model):
    name = models.CharField(
        "Название.",
        max_length=200,
        help_text="Укажите название.",
    )

    def __str__(self):
        return self.name


class TransactionItemModel(ItemModel):
    currency = models.CharField(
        "Валюта",
        choices=CURRENCY,
        max_length=5,
        default=CURRENCY[0][0],
        help_text="Выберите валюту из списка."
    )

    sum_of_expense = models.PositiveIntegerField(
        "Сумма",
        help_text="Укажите сумму."
    )

    pub_date = models.DateTimeField(
        "Время занесения",
        default=timezone.now,
        editable=True
    )

    comment = models.TextField(
        "Комментарий",
        null=True,
        blank=True,
        help_text="Добавьте комментарий."
    )
