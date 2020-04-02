
from django.urls import path
from django.contrib.auth.views import login as auth_view
from . import views

app_name='account'

urlpatterns = [
    # path('login/', auth_view.LoginView.as_view(), name='login'),
    # path('password_change/', auth_view.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', auth_view.LoginView.as_view(), name='password_change_done'),
    # path('password_reset/', auth_view.LoginView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_view.LoginView.as_view(), name='password_reset_done'),
    # path('password_reset/confirmed/<uid64>/<token>/', auth_view.LoginView.as_view(), name='password_reset_confirm'),
    # path('password_reset/complete/', auth_view.LoginView.as_view(), name='password_reset_complete'),
]