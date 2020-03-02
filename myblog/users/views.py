from django.shortcuts import render
from django.views import View


# Create your views here.

# 登录页面视图
class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        pass
