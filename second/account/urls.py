from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup , name='signup' ),
    path('signup_func/', signup_func, name='signup_func'),
    path('login/', login , name='login' ),
    path('login_func/', login_func, name='login_func'),
]