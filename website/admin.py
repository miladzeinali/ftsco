from django.contrib import admin
from .models import TyreHandler,CylinderHandler,StrutHandler,category,message,post,\
    Wheelmotor,PipeHandler,BeltHandler,RodHandler,CableHandler

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

class PipeHandlerAdmin(admin.ModelAdmin):
    list_display = ('id','code','model_Year')
    search_fields = ('id','code','model_Year','name')

class BeltHandlerAdmin(admin.ModelAdmin):
    list_display = ('id','code','model_Year')
    search_fields = ('id','code','model_Year','name')

class WheelmotorAdmin(admin.ModelAdmin):
    list_display = ('id','code','model_Year')
    search_fields = ('id','code','model_Year','name')

class RodHandlerAdmin(admin.ModelAdmin):
    list_display = ('id','code','model_Year')
    search_fields = ('id','code','model_Year','name')

class CableHandlerAdmin(admin.ModelAdmin):
    list_display = ('id','code','model_Year')
    search_fields = ('id','code','model_Year','name')

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
admin.site.register(Wheelmotor,WheelmotorAdmin)
admin.site.register(RodHandler,RodHandlerAdmin)
admin.site.register(CableHandler,CableHandlerAdmin)
admin.site.register(PipeHandler,PipeHandlerAdmin)
admin.site.register(BeltHandler,BeltHandlerAdmin)
admin.site.register(category,CategoryAdmin)
admin.site.register(message,messageAdmin)
admin.site.register(post,postAdmin)
