from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup , name='signup' ),
    path('login/', login_view , name='login_view' ),
    path('logout_view',logout_view , name ='logout_view'),
]