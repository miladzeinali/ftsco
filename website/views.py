from django.shortcuts import render
from .models import TyreHandler,CylinderHandler,StrutHandler

# Create your views here.


def home(request):
    return render(request,'pages/home.html',{'alo':[]})

def tyreHandler(request):
    tyrehandlers=TyreHandler.objects.all()
    count=len(tyrehandlers)
    return render(request, 'webproduct/listproduct.html', {'products':tyrehandlers, 'count':count})

def cylinderHandler(request):
    cylinderhandlers=CylinderHandler.objects.all()
    count=len(cylinderhandlers)
    return render(request,'webproduct/listproduct.html',{'products':cylinderhandlers,'count':count})

def strutHandler(request):
    struthandlers=StrutHandler.objects.all()
    count=len(struthandlers)
    return render(request,'webproduct/listproduct.html',{'products':struthandlers,'count':count})
