from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category')
    search_fields = ('id','category')

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','subtitle','category')
    search_fields = ('id','title')

class SliderAdmin(admin.ModelAdmin):
    list_display = ('id','text')
    search_fields = ('id','text')

class NewsProductAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('id','name')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','name','comment','approved')
    search_fields = ('id','name','comment')

class MailAdmin(admin.ModelAdmin):
    list_display = ('id','name','title')
    search_fields = ('id','name','title')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Slider,SliderAdmin)
admin.site.register(NewsProduct,NewsProductAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Mail,MailAdmin)