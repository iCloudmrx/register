from django.urls import path
from .views import post,post_detail


urlpatterns=[
    path('',post,name='post'),
    path('<str:slug>/',post_detail,name='post_detail'),
]