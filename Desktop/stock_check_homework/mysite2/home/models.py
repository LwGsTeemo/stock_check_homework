from django.db import models

# 依照每支股票,建立資料庫內容的欄位資料型態

class c6180(models.Model): #橘子
    date = models.DateTimeField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    change = models.FloatField(blank=True, null=True)
    transaction = models.IntegerField(blank=True, null=True)



class c2002(models.Model): #中鋼
    date = models.DateTimeField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    change = models.FloatField(blank=True, null=True)
    transaction = models.IntegerField(blank=True, null=True)



class c2317(models.Model): #鴻海
    date = models.DateTimeField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    change = models.FloatField(blank=True, null=True)
    transaction = models.IntegerField(blank=True, null=True)



class c2330(models.Model): #台積電
    date = models.DateTimeField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    change = models.FloatField(blank=True, null=True)
    transaction = models.IntegerField(blank=True, null=True)



class c2377(models.Model): #微星
    date = models.DateTimeField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    change = models.FloatField(blank=True, null=True)
    transaction = models.IntegerField(blank=True, null=True)



class c2603(models.Model): #長榮
    date = models.DateTimeField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    change = models.FloatField(blank=True, null=True)
    transaction = models.IntegerField(blank=True, null=True)



class c2609(models.Model): #陽明
    date = models.DateTimeField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    change = models.FloatField(blank=True, null=True)
    transaction = models.IntegerField(blank=True, null=True)



class c2886(models.Model): #兆豐金
    date = models.DateTimeField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    change = models.FloatField(blank=True, null=True)
    transaction = models.IntegerField(blank=True, null=True)



class c3008(models.Model): #大立光
    date = models.DateTimeField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    change = models.FloatField(blank=True, null=True)
    transaction = models.IntegerField(blank=True, null=True)



class c3260(models.Model): #威剛
    date = models.DateTimeField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    change = models.FloatField(blank=True, null=True)
    transaction = models.IntegerField(blank=True, null=True)

