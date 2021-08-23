from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=35)

class Post(models.Model):
    title = models.CharField(max_length=85)
    subtitle = models.CharField(max_length=85)
    image1 = models.ImageField(upload_to='posts',null=True,blank=True)
    image2 = models.ImageField(upload_to='posts',null=True,blank=True)
    image3 = models.ImageField(upload_to='posts',null=True,blank=True)
    summary = models.TextField(max_length=150)
    text = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    likes = models.PositiveSmallIntegerField(default=0)
    tag = models.CharField(max_length=50)

class Slider(models.Model):
    image = models.ImageField(upload_to='slider')
    text = models.CharField(max_length=20)

class NewsProduct(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='newsProduct')

class Comment(models.Model):
    name = models.CharField(max_length=30)
    comment = models.TextField(max_length=150)
    approved = models.BooleanField(default=False)
    likes = models.PositiveSmallIntegerField(default=0)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

class Mail(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=35)
    text = models.TextField(max_length=150)

