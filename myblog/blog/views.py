from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# 用于测试的代码
# def index(request):
#     return HttpResponse("hahaha")

# index页面
class IndexView(View):

    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        pass

class IndexTwoView(View):

    def get(self, request):
        return render(request, 'index2.html')

    def post(self, request):
        pass

class View(View):

    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        pass