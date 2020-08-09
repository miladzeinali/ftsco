from django.shortcuts import render
from .models import TyreHandler,CylinderHandler,StrutHandler

# Create your views here.


def home(request):
    return render(request,'pages/home.html',{'alo':[]})

def tyreHandler(request):
    tyrehandlers=TyreHandler.objects.all()
    return render(request,'webproduct/tyrehandlers.html',{'tyrehandler':tyrehandlers})

def cylinderHandler(request):
    cylinderhandlers=CylinderHandler.objects.all()
    return render(request,'webproduct/cylinderhandlers.html',{'cylinderhandlers':cylinderhandlers})

def strutHandler(request):
    struthandlers=StrutHandler.objects.all()
    return render(request,'webproduct/struthandlers.html',{'struthandlers':struthandlers})
