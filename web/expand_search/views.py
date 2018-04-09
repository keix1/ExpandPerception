from django.http import HttpResponse
from django.shortcuts import render
import sys,os
sys.path.append('expand_search/modules/testmodu')
sys.path.append('expand_search/modules/search')
from modu import hello
from expandsearch import ExpandSearch
from .forms import MyForm

def index(request):

    app = hello()
    view_list = []
    # return HttpResponse("Hello, world. You're at the blog index.")
    if request.method == "POST":
        form = MyForm(data=request.POST)  # ← 受け取ったPOSTデータを渡す
        if form.is_valid():  # ← 受け取ったデータの正当性確認
            text = request.POST['text']  # ← 正しいデータを受け取った場合の処理
            es = ExpandSearch()
            es_list = es.get_expand(text)
            view_list = es_list

    else:  # ← methodが'POST'ではない = 最初のページ表示時の処理
        form = MyForm()

    myapp_data = {
    'app': app,
    'view_list': view_list,
    'form': form
    }
 
    return render(request, 'index.html', myapp_data)

def getExpand(request):
    myapp_data = {
        'words': 'aaa',
    }

    return render(request, 'expand.html', myapp_data)