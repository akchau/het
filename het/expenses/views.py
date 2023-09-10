from django.shortcuts import render

# Create your views here.
def bill(request):
    """Главная страница. Включено кеширование"""
    template = "expenses/bill.html"
    context = {
        "title": "Список расходов",
        "header": "Список расходов"
    }
    return render(request, template, context)