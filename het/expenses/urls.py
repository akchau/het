from django.urls import include, path
from . import views
app_name = "expenses"

urlpatterns = [
    path('bill/', views.bill, name="bill")
]