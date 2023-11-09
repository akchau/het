from django.urls import path
from django.contrib.auth import views
from . import views as custom_view
app_name = "users"

urlpatterns = [
    path('account/<int:pk>/', custom_view.account, name='account'),
    path('signup/', custom_view.SignUp.as_view(), name='signup'),
    # Авторизация
    path(
        'login/',
        views.LoginView.as_view(template_name='users/pages/login.html'),
        name='login'
    ),

    # Выход
    path(
        'logout/',
        views.LogoutView.as_view(
            template_name='users/pages/logout.html'),
        name='logout'
    ),

    # Смена пароля
    path(
        'password_change/',
        views.PasswordChangeView.as_view(
            template_name='users/pages/password_change.html'),
        name='password_change'
    ),

    # Сообщение об успешном изменении пароля
    path(
        'password_change/done/',
        views.PasswordChangeDoneView.as_view(),
        name='password_change_done'
    ),

    # Восстановление пароля
    path(
        'password_reset/',
        views.PasswordResetView.as_view(),
        name='password_reset'
    ),

    # Сообщение об отправке ссылки для восстановления пароля
    path(
        'password_reset/done/',
        views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),

    # Вход по ссылке для восстановления пароля
    path(
        'reset/<uidb64>/<token>/',
        views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),

    # Сообщение об успешном восстановлении пароля
    path(
        'reset/done/',
        views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
]
