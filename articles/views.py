from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms

# Create your views here.
def treasure_trove(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'articles/treasure_trove.html',{'treasure_trove':articles})
def article_detail(request,slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'article':article})

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            #save article to db
            condition = form.save(commit=False)
            condition.author = request.user
            condition.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request,'articles/article_create.html',{'form':form})
