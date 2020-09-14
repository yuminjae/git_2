from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
import datetime

# Create your views here.
def home(request):
    return render(request, "index.html")

def about(request):
    user_id = request.GET['id']
    password = request.GET['password']
    

    return render(request, 'about.html',{'user_id' :user_id, 'passowrd': password})

def view(request): 
    content = Blog.objects.all()
    return render(request, 'view.html', {'content': content})

def detail(request, blog_id):
    obj = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'obj': obj})

def new(request):
    return render(request, "new.html")

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.pub_date = datetime.datetime.now()
    blog.body = request.GET['content']
    blog.save()
    return redirect('/view')

def update(request, blog_id):
    obj = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'update.html', {'blog':obj})

def updateAction(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.title = request.GET['title']
    blog.pubdate_date = datetime.datetime.now()
    blog.body = request.GET['content']
    blog.save()
    return redirect('/view')

def delete(request, blog_id):
    get_object_or_404(Blog, pk=blog_id).delete()

    return redirect('/view')