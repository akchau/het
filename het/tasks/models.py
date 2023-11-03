from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Task(models.Model):

    CREATE = 'CR'
    DONE = 'DN'
    TASK_STATUS = [
        (CREATE, 'Cоздана'),
        (DONE, 'Выполнена'),
    ]

    status = models.CharField(
        "Статус задачи",
        choices=TASK_STATUS,
        max_length=40
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name="Пользователь",
    )

    regularity = models.SmallIntegerField(
        "Регулярность",
    )

    text = models.CharField(
        "Текст задачи",
        max_length=200,
    )

    date = models.DateField(
        "Дата задачи"
    )

    @property
    def next_data(self):
        return self.date + self.regularity

    class Meta:
        ordering = ("text",)
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
