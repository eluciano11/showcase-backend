from django.conf.urls import patterns

from . import views

urlpatterns = patterns(
    # Prefix
    '',
    (
        r'auth/login$',
        views.LoginView.as_view()
    ),
    (
        r'auth/signup$',
        views.SignupView.as_view()
    ),
    (
        r'auth/forgot_password$',
        views.ForgotPasswordView.as_view()),
    (
        r'auth/reset_password$',
        views.ResetPasswordView.as_view()
    ),
    (
        r'users/me$',
        views.UserSettingsView.as_view()
    ),
    (
        r'users/me/change_password$',
        views.ChangePasswordView.as_view()
    ),
)
