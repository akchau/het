from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path('done/<int:pk>/', views.done, name="done"),
]