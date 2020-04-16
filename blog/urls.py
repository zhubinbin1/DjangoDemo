"""DjangoDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^hello/$', views.hello),
    # path函数将url映射到视图
    path('', views.article_list, name='article_list'),
    path('article_list/', views.article_list, name='article_list'),
    path('article_detail/<int:id>/', views.article_detail, name='article_detail'),
    path('article_create/', views.article_create, name='article_create'),
    # 删除文章
    path('article_delete/<int:id>/', views.article_delete, name='article_delete'),
    # 安全删除文章
    path('article_safe_delete/<int:id>/', views.article_safe_delete, name='article_safe_delete'
         ),
    # 更新文章
    path('article_update/<int:id>/', views.article_update, name='article_update'),
]
