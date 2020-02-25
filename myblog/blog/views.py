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
# index2页面
class IndexTwoView(View):

    def get(self, request):
        return render(request, 'index2.html')

    def post(self, request):
        pass
# about页面
class AboutView(View):

    def get(self, request):
        return render(request, 'about.html')

    def post(self, request):
        pass

# author页面
class AuthorView(View):

    def get(self, request):
        return render(request, 'author.html')

    def post(self, request):
        pass

# authors页面
class AuthorsView(View):

    def get(self, request):
        return render(request, 'authors.html')

    def post(self, request):
        pass

# blog-detail页面
class BlogDetailView(View):

    def get(self, request):
        return render(request, 'blog-details.html')

    def post(self, request):
        pass


# contact页面
class ContactView(View):

    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        pass


# guide页面
class GuideView(View):

    def get(self, request):
        return render(request, 'guide.html')

    def post(self, request):
        pass


# tag页面
class TagView(View):

    def get(self, request):
        return render(request, 'tag.html')

    def post(self, request):
        pass

# tags页面
class TagsView(View):

    def get(self, request):
        return render(request, 'tags.html')

    def post(self, request):
        pass