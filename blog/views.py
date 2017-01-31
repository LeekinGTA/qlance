from django.shortcuts import render
from . import models

def index(request):
    articles = models.Article.objects.all()
    return render(request,"blog/index.html",{'articles':articles})


def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, "blog/article_page.html",{'article':article})

def editorPage(request):

    return render(request, "blog/EditorPage.html")

def addArticle(request):
    #get form table request value
    title = request.POST.get('title',"TITLE")
    content = request.POST.get('content',"CONTENT")
    # write data to the database
    isok=models.Article.objects.create(title=title,content=content)
    print isok
    # add success back index page
    articles = models.Article.objects.all()
    return render(request,"blog/index.html",{'articles':articles})
