from django.contrib import admin
from .models import TyreHandler,CylinderHandler,StrutHandler,tyreHandlerImages,\
    StrutHandlerImages,CylinderHandlerImages
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


admin.site.register(TyreHandler,TyreHandlerAdmin)
admin.site.register(CylinderHandler,CylinderHandlerAdmin)
admin.site.register(StrutHandler,StrutHandlerAdmin)
admin.site.register(tyreHandlerImages,tyreHandlerImagesAdmin)
admin.site.register(StrutHandlerImages,StrutHandlerImagesAdmin)
admin.site.register(CylinderHandlerImages,cylinderhandlerImagesAdmin)

