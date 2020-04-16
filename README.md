

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
```text
form 操作
当视图函数接收到一个客户端的request请求时，首先根据request.method判断用户是要提交数据（POST）、还是要获取数据（GET）：
如果用户是提交数据，将POST给服务器的表单数据赋于article_post_form实例。然后使用Django内置的方法.is_valid()判断提交的数据是否满足模型的要求。
如果满足要求，保存表单中的数据（但是commit=False暂时不提交到数据库，因为author还未指定），
并指定author为id=1的管理员用户。然后提交到数据库，并通过redirect返回文章列表。redirect可通过url地址的名字，反向解析到对应的url。
如果不满足要求，则返回一个字符串"表单内容有误，请重新填写。"，告诉用户出现了什么问题。
如果用户是获取数据，则返回一个空的表单类对象，提供给用户填写。<form>..</form>标签中的内容就是需要提交的表单。method="post"指定了表单提交的方式为POST
（与视图函数中的request.method相联系）；action="."指定了表单提交的地址为默认的当前url。
关于{% csrf_token %}，它是Django中一个与网络安全相关的中间件验证。目前我们暂时不去深究它的实现，
只需要知道表单中必须包含它就可以了，否则将会得到一个403错误。
<input>和<textarea>标签中的name=''属性指定了当前文本框提交的数据的名称，
它必须与表单类中的字段名称对应，否则服务器无法将字段和数据正确的对应起来
Layer弹窗组件
到官网下载Layer插件：Layer
解压后将里面的layer文件夹（含有layer.js的）直接复制到项目的static文件夹下
csrf_token
攻击者盗用了你的身份，以你的名义发送恶意请求。还是拿删除文章举例：
用户登录了博客网站A，浏览器记录下这次会话，并保持了登录状态；
用户在没有退出登录的情况下，又非常不小心的打开了邪恶的攻击网站B；
攻击网站B在页面中植入恶意代码，悄无声息的向博客网站A发送删除文章的请求，
此时浏览器误以为是用户在操作，从而顺利的执行了删除操作。

```








