from abc import ABC
from enum import Enum
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from core import views as core_views

from .forms import CreationForm, EmailChangeForm, UserInfoChangeForm
from . import exceptions


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/pages/signup.html'


class AccountFnction(str, Enum):
    PERSONAL_DATA = "personal_data"
    EMAIL = "email"
    CHANGE_PASSWORD = "change_password"
    CHANGE_PASSWORD_DONE = "change_password_done"
    DROPPING_PASSWORD = "dropping_password"
    DROPPING_PASSWORD_RESET_LINK_DONE = "dropping_password_reset_link_done"


class CardText(str, Enum):
    CHANGE_PASSWORD_DONE = "Успешно!"
    DROPPING_PASSWORD_RESET_LINK_DONE = "Успешно!"


class CardHeader(str, Enum):
    CHANGE_PASSWORD_DONE = "Ваш пароль изменен!"
    DROPPING_PASSWORD_RESET_LINK_DONE = ("Вам на почту отправлена"
                                         "ссылка для сброса пароля!")


class FormHeader(str, Enum):
    PERSONAL_DATA = "Изменение основных данных профиля"
    EMAIL = "Изменение email"
    CHANGE_PASSWORD = "Смена пароля"
    DROPPING_PASSWORD = "Сброс пароля"


PAGE_CONTEXT = {
    AccountFnction.PERSONAL_DATA: {
        "form": UserInfoChangeForm,
        "header": FormHeader.PERSONAL_DATA,
        "is_instance": True
    },
    AccountFnction.EMAIL: {
        "form": EmailChangeForm,
        "header": FormHeader.EMAIL,
        "is_instance": True
    },
    AccountFnction.CHANGE_PASSWORD: {
        "form": PasswordChangeForm,
        "header": FormHeader.CHANGE_PASSWORD,
        "is_instance": False
    },
    AccountFnction.DROPPING_PASSWORD: {
        "form": PasswordResetForm,
        "header": FormHeader.DROPPING_PASSWORD,
        "is_instance": False
    },
    AccountFnction.CHANGE_PASSWORD_DONE: {
        "header": CardHeader.CHANGE_PASSWORD_DONE,
        "card_text": CardText.CHANGE_PASSWORD_DONE
    },
    AccountFnction.DROPPING_PASSWORD_RESET_LINK_DONE: {
        "header": CardHeader.DROPPING_PASSWORD_RESET_LINK_DONE,
        "card_text": CardText.DROPPING_PASSWORD_RESET_LINK_DONE
    }
}


class BaseConstructor(ABC):

    def __init__(self, section_name: str, object):
        self.current_section = self.clean_section_name(value=section_name)
        self.object = object

    @property
    def BASE_TEMPLATE_COMPONENTS_PATH(self):
        raise NotImplementedError

    @property
    def CONTEXT(self):
        raise NotImplementedError

    def clean_section_name(self, value: str):
        print(value)
        if (isinstance(value, str) and
           value in [member.value for member in AccountFnction]):
            return value
        elif (value is None or
              (isinstance(value, str) and
               value not in [member.value for member in AccountFnction])):
            return None
        else:
            raise exceptions.SectionNotFoundException(name=value)

    @property
    def form(self):
        if self.current_section:
            if self._form_class and self._is_instance is True:
                return self._form_class(None, instance=self.object)
            elif self._form_class and self._is_instance is False:
                return self._form_class(None)
        return None

    @property
    def template_component(self):
        if self.current_section and self.form is not None:
            return os.path.join(
                os.path.join(
                    self.BASE_TEMPLATE_COMPONENTS_PATH,
                    "forms",
                ),
                f"{self.current_section}.html"
            )
        elif self.current_section and self.form is None:
            return os.path.join(
                os.path.join(
                    self.BASE_TEMPLATE_COMPONENTS_PATH,
                    "cards",
                ),
                f"{self.current_section}.html"
            )
        else:
            return None

    @property
    def header(self):
        if self.current_section:
            card_header = self._request_context.get("header")
            if (card_header.value and
               isinstance(card_header.value, str)):
                return card_header.value
            raise exceptions.NotCorrectHeadException
        else:
            return None

    @property
    def _request_context(self):
        if isinstance(self.CONTEXT, dict):
            CURRENT_CONTEXT = self.CONTEXT[self.current_section]
            if isinstance(CURRENT_CONTEXT, dict):
                return CURRENT_CONTEXT
        raise exceptions.NotCorrectContextDictException

    @property
    def _form_class(self):
        return self._request_context.get("form")

    @property
    def _is_instance(self):
        return self._request_context.get("is_instance")


class AcountConstructor(BaseConstructor):
    BASE_TEMPLATE_COMPONENTS_PATH = "users/components/accounts/"
    CONTEXT = PAGE_CONTEXT


@login_required
def account(request):
    template = 'users/pages/account.html'
    current_section = request.GET.get('current_section', None)
    CONSTRUCTOR = AcountConstructor(
        section_name=current_section,
        object=request.user
    )
    context = {
        "user_pk": request.user.pk,
        "username": request.user.username,
        "title": request.user.username,
        "header": request.user.username,
        "current_section": CONSTRUCTOR.current_section,
        "form": CONSTRUCTOR.form,
        "form_header": CONSTRUCTOR.header,
        "template_component": CONSTRUCTOR.template_component
    }
    return render(request, template, context)


@login_required
def edit(request, pk: int):
    return core_views.edit_obj(
        request=request,
        pk=pk,
        form_class=UserInfoChangeForm
    )
