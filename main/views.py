from django.shortcuts import render,get_object_or_404
from main import models
from main import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def index(request):
    latest_articles=models.Article.objects.all().order_by('-createdAt')[:20]
    context ={
        "latest_articles":latest_articles
    }
    return render(request,'main/index.html',context)
def article(request,pk):

    if request.method == "POST":

        c1 = models.comment(comments = request.POST['Comment'])
        c1.save()

        models.Article.objects.get(pk = pk).comments.add(c1)



    Comment = models.Article.objects.get(pk = pk).comments.all()
    
        

    article = models.Article.objects.get(pk = pk)
    context= {  
        "article" : article,
        "comment" : Comment
        

        }
    return render(request, 'main/article.html',context)

def author(request,pk):
        author = get_object_or_404(models.Author,pk = pk)
        context= {
            "author" : author

        }
        return render(request,'main/author.html',context)

@login_required(login_url='/login/')
def create_article(request):
    authors = models.Author.objects.all()
    context={
            "authors" : authors
    }
    if request.method == "POST":
        article_data = {
            "title": request.POST['title'],
            "content": request.POST['content'],
            "category":request.POST['category']
        }
        article = models.Article.objects.create(**article_data)
        author =  models.Author.objects.filter(pk = request.POST['author'])
        article.authors.set(author)
        context["success"]=True
    return render(request,'main/create_article.html',context)


def create_author(request):
    create_auth = forms.CreateAuthor()
    if request.method == "POST":
        authorForm = forms.CreateAuthor(request.POST)
        if authorForm.is_valid():
            authorForm.save()
            return HttpResponseRedirect('/article')

    context ={
        "create_auth":create_auth
    }
    #if request.method == "POST":
        #author_data = {
            #"name": request.POST['name']
        #}
        #models.Author.objects.create(**author_data)
        #context["succcess"]=True
    return render(request,'main/create_author.html',context)

def home(request):
    return render(request,'main/home.html')

@login_required(login_url='/login/')
def view_authors(request):
    authors = models.Author.objects.all()
    context={
            "authors" : authors
    }
    return render(request,'main/view_authors.html',context)

@login_required(login_url='/login/')
def search(request):
    if request.method == 'GET':
        searchItem = request.GET.get('search')
        try:
            searchFound = models.Article.objects.filter(category__icontains=searchItem)
            return render(request, 'main/search.html', {"searchItems":searchFound,"term":searchItem}) 
        except:
            return render(request,"main/search.html",{'searchItems':searchFound,"term":searchItem})
    else:
        return render(request, 'main/search.html',{"term":searchItem})