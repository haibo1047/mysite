from django.shortcuts import render

from django.http import HttpResponse,HttpRequest
# Create your views here.

from django.utils import translation
def home(request):
    ctx = {}
    print('home')

    print(translation.get_language())
    return render(request,"home.html",ctx)