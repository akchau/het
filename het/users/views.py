from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CreationForm
from django.views.generic import CreateView


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('users:login')
    template_name = 'users/pages/signup.html'


def account(request):
    template = 'users/pages/account.html'
    current_section = request.GET.get('current_section', 'personal_data')
    context = {
        "user_pk": request.user.pk,
        "username": request.user.username,
        "title": request.user.username,
        "header": request.user.username,
        "current_section": current_section,
    }
    return render(request, template, context)
