from django.shortcuts import render
from django.views import View
from django.utils import timezone
from django.http import HttpResponse


from blog.models import Article
import markdown
import json


# index页面
class IndexView(View):
    def get(self, request):
        # 返回时间
        timeoftoday = timezone.now().date()
        # 返回name
        # # 获取文章
        # article_list = Article.objects.all()
        # article = []
        # for a in article_list:
        #     article.append(a.title)

        # 获取文章
        article_list = Article.objects.all()
        articles = []

        for a in article_list:
            articles.append({
                'articletitle': a.title,
                'articlebread': a.bread,
                'articlecontent': a.content,
                'articletime': a.pub_date,
                'articleid': a.id,
            })

        context = {"zuoyouming": "梦想不大，道路很长，开始了就别停下。",
                   "timeoftoday": timeoftoday,
                   "articles": articles,
                   }

        return render(request, 'index.html', context)

    def post(self, request):
        pass


# about页面
class AboutView(View):

    def get(self, request):
        # 返回时间
        timeoftoday = timezone.now().date()
        # 返回name

        context = {"zuoyouming": "梦想不大，道路很长，开始了就别停下。",
                   "timeoftoday": timeoftoday,

                   }

        return render(request, 'about.html', context)

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


# 404页面
class FourZeroFourView(View):

    def get(self, request):
        return render(request, '404.html')

    def post(self, request):
        pass



