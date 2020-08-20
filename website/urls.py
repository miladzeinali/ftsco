from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('', views.home, name='home'),
    path('products/tyrehandlers', views.tyreHandler, name='tyreh'),
    path('products/cylinderhandlers', views.cylinderHandler, name='cylinderh'),
    path('products/struthandlers', views.strutHandler, name='struth'),
    path('products/pipehandler', views.pipehandler, name='pipe'),
    path('products/belthandler', views.belthandler, name='belt'),
    path('products/wheelmotor', views.wheelmotor, name='wheel'),
    path('products/detailcontrol/<int:id>/<str:type>/', views.productcontrol, name='productcontrol'),
    path('products/tyrehandlers/<int:id>/', views.tyrehandler_detail, name='tyrehdetail'),
    path('products/struthandlers/<int:id>/', views.struthandler_detail, name='strutdetail'),
    path('products/cylinderhandlers/<int:id>/', views.cylinderhandler_detail, name='cylinderdetail'),
    path('products/pipehandler/<int:id>/', views.pipehandler_detail, name='pipedetail'),
    path('products/belthandler/<int:id>/', views.belthandler_detail, name='beltdetail'),
    path('products/wheelmotor/<int:id>/', views.wheelmotor_detail, name='wheeldetail'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('contact/messages/',views.messages,name='message'),
    path('posts/',views.history,name='post'),
]
