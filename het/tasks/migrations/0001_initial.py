# Generated by Django 4.2.5 on 2023-09-17 00:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('CR', 'Cоздана'), ('DN', 'Выполнена')], max_length=40, verbose_name='Статус задачи')),
                ('regularity', models.SmallIntegerField(verbose_name='Регулярность')),
                ('text', models.CharField(max_length=200, verbose_name='Текст задачи')),
                ('date', models.DateField(verbose_name='Дата задачи')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'ordering': ('text',),
            },
        ),
    ]