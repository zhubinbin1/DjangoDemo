#!/usr/bin/python3
# coding:utf-8
# Author binbin
# @Time 2020-04-15 18:49
# IDE PyCharm

from django import forms
from .models import ArticlePost


# 写文章的表单类
class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = ArticlePost
        # 定义表单包含的字段
        fields = ('title', 'body')
