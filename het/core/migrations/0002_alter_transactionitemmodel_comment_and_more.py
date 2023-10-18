# Generated by Django 4.2.5 on 2023-09-17 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionitemmodel',
            name='comment',
            field=models.TextField(blank=True, help_text='Добавьте комментарий.', null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='transactionitemmodel',
            name='currency',
            field=models.CharField(choices=[('RUB', 'RUB')], default='RUB', help_text='Выберите валюту из списка.', max_length=5, verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='transactionitemmodel',
            name='sum_of_expense',
            field=models.PositiveIntegerField(help_text='Укажите сумму.', verbose_name='Сумма'),
        ),
    ]
