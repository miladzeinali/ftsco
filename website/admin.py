from django.contrib import admin
from .models import TyreHandler,CylinderHandler
# Register your models here.


class TyreHandlerAdmin(admin.ModelAdmin):
    list_display = ('id','code','model_Year')
    search_fields = ('id','code','model_Year','name')

class CylinderHandlerAdmin(admin.ModelAdmin):
    list_display = ('id','code','model_Year')
    search_fields = ('id','code','model_Year','name')

admin.site.register(TyreHandler,TyreHandlerAdmin)
admin.site.register(CylinderHandler,CylinderHandlerAdmin)