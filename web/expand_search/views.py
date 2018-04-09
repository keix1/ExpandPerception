from django.http import HttpResponse
from django.shortcuts import render
import sys,os
sys.path.append('expand_search/modules/testmodu')
from modu import hello

def index(request):
    # return HttpResponse("Hello, world. You're at the blog index.")
    myapp_data = {
    'app': hello(),
    'num': range(10),
    }
    return render(request, 'index.html', myapp_data)

def getExpand(request):
    myapp_data = {
        'words': 'aaa',
    }

    return render(request, 'expand.html', myapp_data)