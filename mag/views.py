from django.shortcuts import render
from .models import *
import random

def home(request):
    posts = Post.objects.all()
    # posts = random.choice(post)
    news = posts[0:5]
    top = sorted(posts,key=lambda x: x.likes)
    slider = Slider.objects.all()[0:3]
    # newpro = NewsProduct.objects.latest()
    newpro = NewsProduct.objects.all()
    return render(request,'mags/pages/home.html',{'posts':posts,'news':news,'top':top,'slider':slider,'newspro':newpro})

def Detail(request,id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post,approved=True)
    return render(request,'mags/pages/detail.html',{'post':post,'comments':comments})

def technology(request):
    posts = Post.objects.filter(category='1')
    return render(request,'mags/pages/technology.html',{'posts':posts})

def safety(request):
    posts = Post.objects.filter(category='2')
    return render(request,'mags/pages/safety.html',{'posts':posts})

def news(request):
    posts = Post.objects.filter(category='3')
    return render(request,'mags/pages/news.html',{'posts':posts})

def exhibition(request):
    posts = Post.objects.filter(category='4')
    return render(request,'mags/pages/exhibition.html',{'posts':posts})

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

def video(request):
    return render(request,'mags/pages/video-image.html',)







