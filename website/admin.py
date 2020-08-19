from django.contrib import admin
from .models import TyreHandler,CylinderHandler,StrutHandler,tyreHandlerImages,\
    StrutHandlerImages,CylinderHandlerImages,category,message,post
# Register your models here.


class TyreHandlerAdmin(admin.ModelAdmin):
    list_display = ('id','code','model_Year')
    search_fields = ('id','code','model_Year','name')

class CylinderHandlerAdmin(admin.ModelAdmin):
    list_display = ('id','code','model_Year')
    search_fields = ('id','code','model_Year','name')

class StrutHandlerAdmin(admin.ModelAdmin):
    list_display = ('id','code','model_Year')
    search_fields = ('id','code','model_Year','name')

class tyreHandlerImagesAdmin(admin.ModelAdmin):
    list_display = ('id','tyreHandler')
    search_fields = ('id','tyreHandler')

class cylinderhandlerImagesAdmin(admin.ModelAdmin):
    list_display = ('id','cylinderhandler')
    search_fields = ('id','cylinderhandler')

class StrutHandlerImagesAdmin(admin.ModelAdmin):
    list_display = ('id','struthandler')
    search_fields = ('id','struthandler')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','type')
    search_fields = ('id','type')

class messageAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','message')
    search_fields = ('id','name','phone','message')

class postAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    search_fields = ('id','title')

admin.site.register(TyreHandler,TyreHandlerAdmin)
admin.site.register(CylinderHandler,CylinderHandlerAdmin)
admin.site.register(StrutHandler,StrutHandlerAdmin)
admin.site.register(tyreHandlerImages,tyreHandlerImagesAdmin)
admin.site.register(StrutHandlerImages,StrutHandlerImagesAdmin)
admin.site.register(CylinderHandlerImages,cylinderhandlerImagesAdmin)
admin.site.register(category,CategoryAdmin)
admin.site.register(message,messageAdmin)
admin.site.register(post,postAdmin)
