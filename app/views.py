from django.shortcuts import render

# Create your views here.
import datetime
def filters(request):
    da=datetime.datetime.now()
    d={'data':'HI HeLLo hOw aRe You','da':da,'c':9}
    return render(request,'filters.html',d)

def usd(request):
    d={'data':'HI HeLLo hOw aRe You'}
    return render(request,'usd.html',d)