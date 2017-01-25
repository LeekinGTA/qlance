> myblog是使用Django框架，python语言，MySQL作为数据库开发的一个博客系统

# python2.7安装
## windows下安装
* 点击连接下载msi文件，[python2.7](https://www.python.org/downloads/)
* 安装的时候别忘记了安装环境变量，如果你忘记安装，可以手动配置，将python下bin目录添加到系统变量path下
* 打开cmd控制台，输入``python``,应该进入python命令行模式，到这里python安装完成

## Linux安装python,以centos为例
* 在控制台界面输入``sudo yum install python2 ``输入密码等待安装完成，一般情况下linux自带了python，但是要保证版本时python2.7以上，2.7以下的请重新安装。

# 包管理工具pip的安装
## windows下安装pip
* 点击连接进入下载界面,[pip9.0.1](https://pypi.python.org/pypi/pip#downloads)
* 点击下载压缩包，tar.gz,下载完成解压，来到pip目录下执行``python setup.py``进行安装
* 命令行安装完成后在python2.7目录下的script目录下应该可以看到pip.exe文件，将这个文件路径添加到系统path变量当中
* 测试：重启控制台输入pip，不出意外应该输出使用方法，如果出现command not found，那么请检查你的环境变量以及pip是否正确安装。

# 安装Django框架
## pip安装Django
* 控制台输入``pip install Django==1.10.5``,等待安装完成
* 测试是否正确安装，输入``django``查看是否有使用信息输出

# 新建项目
* 进入要新建项目的文件夹，输入``python django-admin.py startproject webapp``创建一个名为webapp的项目
* ``cd webapp``进入项目目录，``dir``查看文件夹中的内容：项目结构如下：
——webapp
 |——manage.py:提供命令行操作项目支持
 |——webapp:存放项目接口以及配置文件等
    |——__init__.py
    |——setting.py:项目配置文件
    |——urls:项目url配置文件
    |——wsgi.py:web服务器与python之间的接口
 |——db.sqlite3:项目默认使用的数据库文件

# 新建应用
* 在manage.py当中打开命令行，输入``python django-admin startapp blog``
* 这时候在项目目录下会新增了blog的应用名，目录结构如下：
——blog
  |——migrations
     |——__init__.py
  |——__init__.py
  |——admin.py:后台管理入口文件
  |——apps.py
  |——models.py:模型文件（django是mvc框架）
  |——tests.py:测试文件
  |——views.py:视图文件

---
到这里，从环境搭建到项目创建基本完成
---

# 使用MySQL作为项目数据库
* 下载python-MySQLdb[MySQLdb-python](https://sourceforge.net/projects/mysql-python/)
* 安装此扩展，并验证是否安装成功，python命令行模式输入``import MySQLdb``如果不报错，就说明已经成功安装扩展
* 同步操作：来到项目根目录，执行``manage.py syncdb``
* 修改setting.py文件：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
#这时django默认的数据库，使用的是sqlite3，把上面的注释掉，并添加：
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myweb_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

```
* 重启服务``python manage.py runserver``,如果不报错说明成功使用MySQL

# 相数据添加数据
* 在应用下的models.py中导入models``from django.db import models``
* 新建一个类，这个类对应数据库当中的一张表，类属性就是表中的字段，如下：
```python
# 文章模型，类属性对应数据库表字段
class Article(models.Model):
    title = models.CharField(max_length=32,default='title')
    content = models.TextField(null=True)
    #title和content是Article表中的字段
```
> 注意：如果要在python当中写中文注释，就需要在文件头使用一行代码来改变编码：``# -*- coding: utf-8 -*-``

## 数据迁移(根据models在数据库中生成相应的表)
```bash
python manage.py makemigrations //在manage.py文件同级目录下执行此命令
```
> 在执行命令：

```bash
python manage.py migrate
```

## 查看数据库表信息
```bash
python manage.py sqlmigrate blog 0001  --0001为表
```

## 数据库读取mysql,在views.py添加操作数据库函数

```python
import models

article = models.Article.objects.get(pk=1)
```

# 后台配置

## 新建超级管理员

```bash
python manage.py createsuperuser
```
## 修改后台语言为中文
> 修改setting.py文件中方的LANGUAGE = 'zh_Hans'

## 配置Admin,新增博客管理页面
* 在应用下admin.py中引入自身的models模块(或者里面的模型类)
* 编辑admin.py 添加：admin.site.register(models.Article)

```python
from models import Article

admin.site.register(Article)
```

## 修改后台``Article object``为文章标题
* 在Article类下添加一个方法
* 根据Python版本:

```python
__str__(self)   #python3
__unicode_(self)   #python2.7
#在方法当中返回
#return self.title
```
