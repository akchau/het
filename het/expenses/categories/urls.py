from django.urls import path
from . import views
app_name = "expenses_categories"

urlpatterns = [
    path('', views.list, name="list"),
    path('new/', views.new, name="new"),
    path('delete/<int:pk>/', views.delete, name="delete")
]
