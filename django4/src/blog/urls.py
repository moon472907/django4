'''
Created on 2019. 5. 4.

@author: 405
'''
from django.urls import path
from blog.views import  *

app_name='blog'

urlpatterns=[
    # 뷰클래스를 url등록시 ,뷰클래스 .as_view함수로 등록함
    path('', Index.as_view() ,name = 'index'),
    path('<int:pk>/', Detail.as_view() ,name = 'detail'),
    path('posting/', Posting.as_view(), name = 'posting'),
    path('search/', PostSearch.as_view(), name='postsearch'),
    ]