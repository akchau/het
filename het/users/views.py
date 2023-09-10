from django.shortcuts import render

# Create your views here.
def account(request):
    """Главная страница. Включено кеширование"""
    template = "users/account.html"
    username = "albert"
    context = {
        "title": "Аккаунт пользователя",
        "username": username,
        "header": "Аккаунт пользователя"
    }
    return render(request, template, context)