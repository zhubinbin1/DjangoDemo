#!/usr/bin/python3
# coding:utf-8
# Author binbin
# @Time 2020-04-16 14:27
# IDE PyCharm


from django.urls import path

from . import views

app_name = 'userprofile'
urlpatterns = [
    # path函数将url映射到视图
    path('login/', views.user_login, name='login'),
    # 用户退出
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    # 用户删除
    path('delete/<int:id>/', views.user_delete, name='delete'),
    # 用户信息
    path('edit/<int:id>/', views.profile_edit, name='edit'),
]
