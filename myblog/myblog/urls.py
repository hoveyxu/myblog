"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, re_path
import blog.urls
from blog import views
urlpatterns = [
    path('', views.IndexView.as_view()),
    re_path('index', views.IndexView.as_view()),

    re_path('about', views.AboutView.as_view()),
    re_path('author', views.AuthorView.as_view()),
    re_path('authors', views.AuthorsView.as_view()),
    re_path('blog-detail', views.BlogDetailView.as_view()),
    re_path('contact', views.ContactView.as_view()),
    re_path('guide', views.GuideView.as_view()),
    re_path('tag', views.TagView.as_view()),
    re_path('tags', views.TagsView.as_view()),
    re_path('404', views.FourZeroFourView.as_view()),
    path('admin/', admin.site.urls),
    url(r'mdeditor/', include('mdeditor.urls')),
]
