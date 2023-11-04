from django.urls import path
from . import views

app_name = "expenses"

urlpatterns = [
    path('my/', views.list, name="list"),
    path('new/', views.new, name="new"),
    path('delete/<int:pk>/', views.delete, name="delete"),
    path('edit/<int:edit_pk>/', views.edit, name="edit")
]
