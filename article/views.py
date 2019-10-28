from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import ArticleForm
from .models import Article
from django.contrib import messages
def index(request):
    context={

        "numbers":[12,3,4,5,6,7]
        
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def dashboard(request):
    articles=Article.objects.filter(author=request.user)
    context={

        "articles":articles
    }
    return render(request,"dashboard.html",context)

def addArticle(request):
    form =ArticleForm(request.POST or None)

    if form.is_valid():
        article=form.save(commit=False)

        article.author=request.user
        article.save()
        messages.success(request,"Başarıyla Kaydedildi.")

        return redirect("index")

    context={
        "form":form
    }
    return render(request,"addarticle.html",context)


def detail(request,id):
    article=get_object_or_404(Article,id=id)

    return render(request,"detail.html",{"article":article})