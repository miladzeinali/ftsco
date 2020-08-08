from django.urls import path
from . import views


app_name='website'
urlpatterns = [
    path('',views.home,name='home'),
    path('products/tyrehandlers',views.tyreHandler,name='tyreh'),
    path('products/cylinderhandlers',views.cylinderHandler,name='cylinderh'),
    path('products/struthandlers',views.strutHandler,name='struth'),
]