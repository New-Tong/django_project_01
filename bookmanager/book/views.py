import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from book.models import BookInfo, PeopleInfo
import re

# Create your views here.

def create_book(request):
    book = BookInfo.objects.create(
        name= 'flask',
        pub_date = '2024-3-18',
        readcount= 10
    )
    return HttpResponse('create')

def shop(request, city_id, shop_id):
    print("city_id:", city_id)
    print("shop_id:", shop_id)
    if not re.match('\d{5}', str(city_id)):
        return HttpResponse('找不到该商品')
    query_params = request.GET
    print(query_params)
    for query_param in query_params:
        print(query_params.getlist(query_param))
    return HttpResponse('shop')

def register(request):
    post_params = request.POST
    print(post_params)
    print(post_params.get('username'))
    print(post_params.get('password'))
    # print('username:', username, ',password:', password)
    return HttpResponse('Register')

def jsondata(request):
    body = request.body
    json_list = json.loads(body.decode())
    print(json_list)
    return HttpResponse('jsondata')

def response(request):
    # response = HttpResponse('res', status=200)
    # response['name'] = 'ShanSong'
    books = [
        {
            'name': 'Django',
            'readcount': 20
        },
        {
            'name': 'Flask',
            'readcount': 10
        }
    ]
    # test_str = 'name:good'
    # response = JsonResponse(data=test_str, safe=False)
    # response = JsonResponse(data=books, safe=False)
    response = redirect('https://www.bilibili.com/')
    return response
    # 1xx   消息
    # 2xx   成功
    # 3xx   重定向
    # 4xx   请求有问题
    # 404   找不到页面，路由有问题
    # 403   禁止访问
    # 5xx   服务器错误

def set_cookie(request):
    params = request.GET
    username = params.get('username')
    response = HttpResponse('set_cookie')
    response.set_cookie('name', value=username)
    return response


def get_cookie(request):
    response = HttpResponse('get_cookie')
    cookies = request.COOKIES
    print(cookies)

    return response 