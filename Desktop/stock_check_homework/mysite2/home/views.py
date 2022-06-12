from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import twstock
from home import models
from datetime import datetime

def index(request):
    '''
    依照html的<form method='post'></form>格式內容所回傳的值來動作
    例如在這邊import twstock,依據回傳的內容去取得股票的資料
    最後再將取得的資料回傳回去html顯示出來
    回傳的內容皆用locals(),將全部的資料打包回傳回去做使用
    '''
    code = request.POST.get("stock_code")
    year = request.POST.get("year")
    month = request.POST.get("month")
    if (year!=None) & (month!=None) :
        year = request.POST.get("year").split(",")
        month = request.POST.get("month").split(",")
        if (year[0]==year[1]) & (month[0]==month[1]) :
            time = "{} / {}".format(year[0], month[0])
        else :
            time = "{} / {} ~ {} / {}".format(year[0], month[0], year[1], month[1])
    if code != None :
        stock = twstock.realtime.get(code)
        open_bar=(float(stock["realtime"]["open"])-float(stock["realtime"]["low"]))/(float(stock["realtime"]["high"])-float(stock["realtime"]["low"]))*100
    year = request.POST.get("year")
    month = request.POST.get("month")
    return render(request, 'index.html', locals())

def search(request):
    '''
    search.html的搜尋時的資料回傳
    '''
    try :
        code = request.POST["stock_code"]
        stock = twstock.realtime.get(code)
        return render(request, 'search.html', locals())
    except :
        return render(request, 'search.html', locals())

def insert(request):
    '''
    建立資料庫內容,在這邊已先將class_list內的每筆資料的欄位型態設定好(在models.py宣告)
    再利用twstock取得長時間的資料,PS:抓資料時須設一下random的間隔時間,以免被網頁ban掉
    最後會得到依據不同股票而建立的10張資料庫table
    '''
    codes = ['6180', '2317', '3008', '2330', '2886', '2002', '3260', '2603', '2377', '2609']
    class_list = [models.c6180, models.c2317, models.c3008, models.c2330, models.c2886, models.c2002, models.c3260, models.c2603, models.c2377, models.c2609]
    for i, code in enumerate(codes) :
        stock = twstock.Stock(code)
        data_list = [class_list[i](**(data._asdict())) for data in stock.fetch_from(2010,1)]
        class_list[i].objects.bulk_create(data_list)
    return HttpResponse('資料庫創建成功')

def candlestick(request):
    '''
    用框架的方式把數據繪圖的資料回傳到candlestick.html主頁上
    在candlestick.html網頁下直接在<script></script>之間寫好程式
    將圖顯示出來
    '''
    try:
        code = request.GET["stock_code"]
        year = request.GET["year"]
        month = request.GET["month"]
        return render(request, 'candlestick.html', locals())
    except:
        return render(request, 'candlestick.html', locals())

def json_data(request):
    '''
    利用建好的資料庫內容,將每筆資料對上各自的股票代碼,利用zip()函式打包成dict
    再透過filter()函式,將所需要的資料從dict抓出來
    因為抓到很多筆資料,所以先將其轉成json格式
    以api的方式引進框架的那個網站
    在candlestick.html上面再讀取json格式
    最後再把圖畫出來
    '''
    code = request.GET["stock_code"]
    year = request.GET["year"].split(",")
    month = request.GET["month"].split(",")
    codes = ['6180', '2317', '3008', '2330', '2886', '2002', '3260', '2603', '2377', '2609']
    class_list = [models.c6180, models.c2317, models.c3008, models.c2330, models.c2886, models.c2002, models.c3260, models.c2603, models.c2377, models.c2609]
    class_dict = dict(zip(codes, class_list))
    data = list(class_dict[code].objects.filter(date__range=((year[0]+"-"+month[0]+"-01"), (year[1]+"-"+month[1]+"-01"))).values("date", "open", "high", "low", "close", "change", "transaction"))
    for i in range(len(data)):
        data[i]["date"] = datetime.strftime(data[i]["date"],'%Y%m%d')
        data[i] = list(data[i].values())
    return JsonResponse(list(data), json_dumps_params={'ensure_ascii':False}, safe=False)

