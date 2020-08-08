from django.urls import path
from . import views


app_name='website'
urlpatterns = [
    path('',views.home,name='home'),
    path('tyrehandlers',views.tyreHandler,name='tyreh'),
    path('cylinderhandlers',views.cylinderHandler,name='cylinderh'),
    path('struthandlers',views.strutHandler,name='struth'),
]