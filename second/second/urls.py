"""
URL configuration for second project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include #include는 다른 거 가져올 떄
from diary.views import home
from account.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home , name="home"),
    path('diary/',include('diary.urls')), #다이어리 앱 다 가져와
    path('signup', signup , name='signup' ),
    path('signup_func', signup_func, name='signup_func'),
    path('login', login , name='login' ),
    path('login_func', login_func, name='login_func'),
]
