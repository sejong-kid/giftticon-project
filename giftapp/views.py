from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import qrcode


@csrf_exempt
def gifticon(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        date = request.POST.get('date')
        name = request.POST.get('name')
        year = date[0:4]
        month = date[4:6]
        day = date[6:8]
        theme = request.POST.get('theme')
        qr = qrcode.make(code)
        qr.save('C://django/기프티콘폼/giftapp/static/bar.jpg')
        if theme == '봄테마':
            return render(request, 'giftapp/span(spring).html' ,  
            {'code':code, 'date':date, 'year':year, 'month':month, 'day':day, 'name':name,'theme':theme})
        elif theme == '여름테마':
            return render(request, 'giftapp/span(summer).html' ,  
            {'code':code, 'date':date, 'year':year, 'month':month, 'day':day,'name':name, 'theme':theme})
        elif theme == '가을테마':
            return render(request, 'giftapp/span(autumn).html' ,  
            {'code':code, 'date':date, 'year':year, 'month':month, 'day':day,'name':name, 'theme':theme})
        elif theme == '겨울테마':
            return render(request, 'giftapp/span(winter).html' , 
            {'code':code, 'date':date, 'year':year, 'month':month, 'day':day,'name':name, 'theme':theme})
    return render(request, 'giftapp/main.html')
# Create your views here.
