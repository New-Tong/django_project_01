# _*_ coding : utf-8 _*_
# @time : 2024/03/16 18:13
# @author : 牛童
# @File : urls.py
# @Project : django_project_01
from django.urls import path
from django.urls import converters
from django.urls.converters import register_converter
from book.views import create_book, shop, register, jsondata, response, set_cookie, get_cookie

class MobileConverter:
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        return value

    def to_str(self, value):
        return value

register_converter(MobileConverter, 'phone')

urlpatterns = [
    path('create/', create_book),
    path('shop/<int:city_id>/<phone:shop_id>/', shop),
    path('register/', register),
    path('jsondata/', jsondata),
    path('res/', response),
    path('set_cookie/', set_cookie),
    path('get_cookie', get_cookie)
]