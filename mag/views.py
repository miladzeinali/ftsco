from django.shortcuts import render
from .models import *

def home(request):
    post = Post.objects.all()
    posts = random.choice(post)
    news = post[0:5]
    top = sorted(post,key=lambda x: x.likes)
    slider = Slider.objects.all()[0:3]
    newpro = NewsProduct.objects.latest()
    return render(request,'home.html',{'posts':posts,'news':news,'top':top,'slider':slider,'newspro':newpro})

def Detail(request,id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post,approved=True)
    return render(request,'detail.html',{'post':post,'comments':comments})

def technology(request):
    posts = Post.objects.filter(category='technology')
    return render(request,'result.html',{'posts':posts})

def safety(request):
    posts = Post.objects.filter(category='safety')
    return render(request,'result.html',{'posts':posts})

def news(request):
    posts = Post.objects.filter(category='news')
    return render(request,'result.html',{'posts':posts})

def exhibition(request):
    posts = Post.objects.filter(category='exhibition')
    return render(request,'result.html',{'posts':posts})

def comment(request,id):
    name = request.POST['name']
    comment = request.POST['comment']
    post = Post.objects.get(id=id)
    Comment.objects.create(name=name,comment=comment,approved=False,likes=0,post=post)

def mail(request):
    name = request.POST['name']
    title = request.POST['title']
    text = request.POST['text']
    Mail.objects.create(name=name,title=title,text=text)







