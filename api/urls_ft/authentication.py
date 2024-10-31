from django.urls import path
from api.views.authentication.forgot_password import ForgotPasswordView
from api.views.authentication.register import RegisterView
from api.views.authentication.login import LoginView
from api.views.authentication.reset_password import PasswordResetConfirmView
from api.views.authentication.logout import LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('reset-password/<str:token>/', PasswordResetConfirmView.as_view(), name='reset_password'),
]
