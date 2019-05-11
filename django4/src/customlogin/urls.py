
from customlogin.views import *
from django.urls import path
app_name='cl'
#도메인 주소 : 127.0.0.1:8000/login/
urlpatterns=[
    #127.0.0.1:8000/login/signup/ -> signup 함수가 호출됨
    path('signup/', signup, name='signup'),
    #127.0.0.1:8000/login/signin/ -> signin 함수가 호출됨
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    ]