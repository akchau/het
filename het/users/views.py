from enum import Enum
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CreationForm, EmailChangeForm, UserInfoChangeForm
from django.views.generic import CreateView


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('users:login')
    template_name = 'users/pages/signup.html'


class AccountFnction(str, Enum):
    PERSONAL_DATA = "personal_data"
    EMAIL = "email"
    CHANGE_PASSWORD = "change_password"
    DROPPING_PASSWORD = "dropping_password"


def account(request):
    template = 'users/pages/account.html'
    current_section = request.GET.get('current_section', None)
    form = None
    if current_section == AccountFnction.PERSONAL_DATA:
        form = UserInfoChangeForm(
            None,
            instance=request.user
        )
    elif current_section == AccountFnction.EMAIL:
        form = EmailChangeForm(
            None,
            instance=request.user
        )
    elif current_section == AccountFnction.CHANGE_PASSWORD:
        form = PasswordChangeForm(
            None,
        )
    elif current_section == AccountFnction.DROPPING_PASSWORD:
        form = PasswordResetForm(
            None
        )
    context = {
        "user_pk": request.user.pk,
        "username": request.user.username,
        "title": request.user.username,
        "header": request.user.username,
        "current_section": current_section,
        "form": form,
    }
    return render(request, template, context)
