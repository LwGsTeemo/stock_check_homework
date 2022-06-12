from home.views import search, candlestick, json_data, index
from django.contrib import admin
from django.urls import path

'''
在urlpatterns後面,可依照在網址後面加上每個path的網址,來切到不同的頁面
要記得先import每個網頁位置(範例: from home.views import candlestick)
'''

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", index),
    # path('search/', search),
    path('candlestick/', candlestick, name="candlestick"),
    path('api/json_data', json_data, name="json_data"),
]
