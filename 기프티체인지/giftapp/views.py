from re import S
from this import s
from django.shortcuts import render
from .models import *
import qrcode
# Create your views here.


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pin = request.POST.get('pin')
        date = request.POST.get('date')

        return render(request, 'giftapp/homepost.html', {'name': name, 'pin': pin, 'date': date})
    else:
        return render(request, 'giftapp/home.html')


def selecttheme(request):
    if request.method == 'POST':
        theme = request.POST.get('whether')
        name = request.POST.get('name')
        pin = request.POST.get('pin')
        date = request.POST.get('date')
        spring = 'spring'
        summer = 'summer'
        autumn = 'autumn'
        winter = 'winter'
        if theme == '봄':
            return render(request, 'giftapp/selectthemepost.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'theme1':spring})
        if theme == '여름':
            return render(request, 'giftapp/selectthemepost.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'theme1':summer})
        if theme == '가을':
            return render(request, 'giftapp/selectthemepost.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'theme1':autumn})
        if theme == '겨울':
            return render(request, 'giftapp/selectthemepost.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'theme1':winter})

    else:
        name = request.GET.get('name')
        pin = request.GET.get('pin')
        date = request.GET.get('date')
        return render(request, 'giftapp/selecttheme.html', {'name': name, 'pin': pin, 'date': date})


def selectimage(request):
    if request.method == 'POST':
        theme = request.POST.get('theme')
        name = request.POST.get('name')
        pin = request.POST.get('pin')
        date = request.POST.get('date')
        img = request.POST.get('img')
        spring = 'spring'
        summer = 'summer'
        autumn = 'autumn'
        winter = 'winter'
        s1 = '봄1'
        s2 = '봄2'
        s3 = '봄3'
        s4 = '봄4'
        su1 = '여름1'
        su2 = '여름2'
        su3 = '여름3'
        su4 = '여름4'
        a1 = '가을1'
        a2 = '가을2'
        a3 = '가을3'
        a4 = '가을4'
        w1 = '겨울1'
        w2 = '겨울2'
        w3 = '겨울3'
        w4 = '겨울4'
        if theme == '봄' and img == '봄1':
            return render(request, 'giftapp/imagepost.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'img': img , 'themeimage': s1 , 'theme' : spring})
        if theme == '여름' and img == '여름1':
            return render(request, 'giftapp/imagepost.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'img': img, 'themeimage': su1 , 'theme' : summer})
        if theme == '가을' and img == '가을1':
            return render(request, 'giftapp/imagepost.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'img': img, 'themeimage': a1, 'theme' : autumn})
        if theme == '겨울' and img == '겨울1':
            return render(request, 'giftapp/imagepost.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'img': img, 'themeimage': w2, 'theme' : winter})

        if theme == '봄' and img == '봄2':
            return render(request, 'giftapp/imagepost.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'img': img,'themeimage': s2, 'theme' :  spring})
        if theme == '여름' and img == '여름2':
            return render(request, 'giftapp/imagepost.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'img': img, 'themeimage': su2 , 'theme' :summer })
        if theme == '가을' and img == '가을2':
            return render(request, 'giftapp/imagepost.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'img': img, 'themeimage': a2, 'theme' : autumn})
        if theme == '겨울' and img == '겨울2':
            return render(request, 'giftapp/imagepost.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'img': img, 'themeimage': w2, 'theme' : winter})

        if theme == '봄' and img == '봄3':
            return render(request, 'giftapp/imagepost.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'img': img, 'themeimage': s3, 'theme' : spring})
        if theme == '여름' and img == '여름3':
            return render(request, 'giftapp/imagepost.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'img': img, 'themeimage': su3, 'theme' :summer })
        if theme == '가을' and img == '가을3':
            return render(request, 'giftapp/imagepost.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'img': img, 'themeimage': a3, 'theme' : autumn})
        if theme == '겨울' and img == '겨울3':
            return render(request, 'giftapp/imagepost.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'img': img, 'themeimage': w3, 'theme' : winter})

        if theme == '봄' and img == '봄4':
            return render(request, 'giftapp/imagepost.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'img': img, 'themeimage': s4, 'theme' : spring})
        if theme == '여름' and img == '여름4':
            return render(request, 'giftapp/imagepost.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'img': img, 'themeimage': su4, 'theme' :summer })
        if theme == '가을' and img == '가을4':
            return render(request, 'giftapp/imagepost.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'img': img, 'themeimage': a3, 'theme' : autumn})
        if theme == '겨울' and img == '겨울4':
            return render(request, 'giftapp/imagepost.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'img': img, 'themeimage': w3, 'theme' : winter})

    else:
        name = request.GET.get('name')
        pin = request.GET.get('pin')
        date = request.GET.get('date')
        theme = request.GET.get('theme')
        spring = '봄'
        summer = '여름'
        autumn = '가을'
        winter = '겨울'
        s1 = '봄1'
        s2 = '봄2'
        s3 = '봄3'
        s4 = '봄4'
        su1 = '여름1'
        su2 = '여름2'
        su3 = '여름3'
        su4 = '여름4'
        a1 = '가을1'
        a2 = '가을2'
        a3 = '가을3'
        a4 = '가을4'
        w1 = '겨울1'
        w2 = '겨울2'
        w3 = '겨울3'
        w4 = '겨울4'
        if theme == '봄':
            return render(request, 'giftapp/selectimage.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'theme1': spring, 'image1':s1, 'image2':s2, 'image3':s3, 'image4':s4})
        elif theme == '여름':
            return render(request, 'giftapp/selectimage.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'theme1': summer, 'image1':su1, 'image2':su2, 'image3':su3, 'image4':su4})
        elif theme == '가을':
            return render(request, 'giftapp/selectimage.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'theme1': autumn, 'image1':a1, 'image2':a2, 'image3':a3, 'image4':a4})
        elif theme == '겨울':
            return render(request, 'giftapp/selectimage.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'theme1': winter, 'image1':w1, 'image2':w2, 'image3':w3, 'image4':w4})


def product(request):
    name = request.GET.get('name')
    pin = request.GET.get('pin')
    date = request.GET.get('date')
    yr = date[0:4]
    mt = date[4:6]
    dt = date[6:8]
    
    theme = request.GET.get('theme')
    img = request.GET.get('img')
    qr = qrcode.make(pin)
    qr.save('C://django/기프티체인지/giftapp/static/bar.jpg')
    return render(request, 'giftapp/product.html', {'theme': theme, 'name': name, 'pin': pin, 'date': date, 'yr':yr, 'mt':mt,'dt':dt ,'img': img})
