from django.urls import include, path
from . import views
app_name = "users"

urlpatterns = [
    path('account/', views.account, name="acconunt")
]