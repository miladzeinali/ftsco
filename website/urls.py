from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('', views.home, name='home'),
    path('products/tyrehandlers', views.tyreHandler, name='tyreh'),
    path('products/cylinderhandlers', views.cylinderHandler, name='cylinderh'),
    path('products/struthandlers', views.strutHandler, name='struth'),
    path('products/detailcontrol/<int:id>/<str:type>/', views.productcontrol, name='productcontrol'),
    path('products/tyrehandlers/<int:id>/', views.tyrehandler_detail, name='tyrehdetail'),
    path('products/struthandlers/<int:id>/', views.struthandler_detail, name='strutdetail'),
    path('products/cylinderhandlers/<int:id>/', views.cylinderhandler_detail, name='cylinderdetail'),
    path('contact/',views.contact,name='contact'),
    path('contact/messages/',views.messages,name='message'),
]
