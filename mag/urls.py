
from django.urls import path
from . import views

app_name = 'mag'
urlpatterns = [
    path('',views.home,name='home'),
    path('detail/<int:id>/',views.Detail,name='detail'),
    path('technology/',views.technology,name='technology'),
    path('safety/',views.safety,name='safety'),
    path('news/',views.news,name='news'),
    path('exhibition/',views.exhibition,name='exhibition'),
    path('comment/',views.comment,name='comment'),
    path('mail/',views.mail,name='mail'),
]

