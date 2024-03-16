# _*_ coding : utf-8 _*_
# @time : 2024/03/16 18:13
# @author : 牛童
# @File : urls.py
# @Project : django_project_01
from django.urls import path

from book.views import index
urlpatterns = [
    path('home/', index),
]