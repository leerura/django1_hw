from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('create', create, name="create" ),
    path('detail/<str:id>',detail, name="detail"), #view의 id 변수 이름 동일하게 !!!
    path('create_func/', create_func, name="create_func"),  #html도 아닌데 URL은 왜 연결하지?
    path('update/<str:update_id>', update, name="update"),
    path('update_func/<str:to_id>', update_fuc, name="update_func"),
    path('delete/<str:delete_id>', delete , name='delete'),
]