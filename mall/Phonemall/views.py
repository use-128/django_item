from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
# Create your views here.
"""
视图就是python函数

"""


def index(request):
    contex = {
        'name':'xhahxahxhadajndkjasnd'
    }

    return render(request,'book/index.html',context=contex)