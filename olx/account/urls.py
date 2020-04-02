
from django.urls import path
from django.contrib.auth.views import login
from . import views

app_name='account'

urlpatterns = [
    # path('login/', login,  {'template_name':'account.login.html'}, name='login')
]