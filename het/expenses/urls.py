from django.urls import path
from . import expense_views, category_views
app_name = "expenses"

urlpatterns = [
    path('expenses/', expense_views.list, name="expenses"),
    path('new_expense/', expense_views.new, name="new_expense"),
    path('delete_expense/<int:pk>/', expense_views.delete, name="delete_expense"),
    path('categories/', category_views.list, name="categories"),
    path('new_category/', category_views.new, name="new_category"),
    path('delete_category/<int:pk>/', category_views.delete, name="delete_category")
]