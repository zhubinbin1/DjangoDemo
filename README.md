

## 创建一个名为app_demo的应用, 在终端项目目录下执行

```text
python3 manage.py startapp app_demo
```
## 启动项目

进入根目录，执行
python manage.py runserver 8080

## 模拟创建一个博客

- https://www.dusaiphoto.com/article/detail/2/

> python3 manage.py startapp blog

- setting中增加blog app
- DjangoDemo 的urls.py 增加 path('blog/', include('blog.urls')),
- blog下创建urls 
    urlpatterns = \[
        url(r'^hello/$', views.hello)
    \]


- blog/views.py 编写
def hello(request):
    return HttpResponse("hello blog")
- 启动服务 python manage.py runserver 8080
- 浏览器访问 http://127.0.0.1:8000/blog/hello/

> 编写module
- 每当对数据库进行了更改（添加、修改、删除等）操作，都需要进行数据迁移。
- 迁移 python manage.py makemigrations
- python manage.py migrate

> 创建管理员账号（Superuser）

- python manage.py createsuperuser

username: binbin
增加文章
> 增加templates 模板

Bootstrap4：
https://code.z01.com/v4/docs/

> 模板语法：

- {% load static %}

    href="{% static 'bootstrap/css/bootstrap.min.css' %}"
    
- href="{% url 'blog:article_list' %}"

- {% load static %}

- {% block title %}
    首页
{% endblock title %}

关于其中的'blog:article_list'的解释：
    前面的blog是在项目根目录的urls.py中定义的app的名称
    后面的article_list是在app中的urls.py中定义的具体的路由地址
    
 <int:id>：Django2.0的path新语法用尖括号<>定义需要传递的参数。这里需要传递名叫id的整数到视图函数中去
 并且id名字和views.py中id名字相同  article_detail(request, id)
 
> 使用Markdown
 
Django出于安全的考虑，会将输出的HTML代码进行转义，这使得article.body中渲染的HTML文本无法正常显示。
管道符|是Django中过滤器的写法，而|safe就类似给article.body贴了一个标签，表示这一段字符不需要进行转义了。
- 代码高亮  
pip install Pygments
Pygments是一种通用语法高亮显示器

> 使用Form表单类发表新文章

