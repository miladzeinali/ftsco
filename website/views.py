from django.shortcuts import render
from .models import TyreHandler, CylinderHandler, StrutHandler


# Create your views here.


def home(request):
    return render(request, 'pages/home.html', {'alo': []})


def tyreHandler(request):
    tyrehandlers = TyreHandler.objects.all()
    count = len(tyrehandlers)
    return render(request, 'webproduct/listproduct.html', {'products': tyrehandlers, 'count': count})


def cylinderHandler(request):
    cylinderhandlers = CylinderHandler.objects.all()
    count = len(cylinderhandlers)
    return render(request, 'webproduct/listproduct.html', {'products': cylinderhandlers, 'count': count})


def strutHandler(request):
    struthandlers = StrutHandler.objects.all()
    count = len(struthandlers)
    return render(request, 'webproduct/listproduct.html', {'products': struthandlers, 'count': count})


def productcontrol(request, id, type):
    if type == 'cylinderhandler':
        return cylinderhandler_detail(request, id)
    elif type == 'struthandler':
        return struthandler_detail(request, id)
    elif type == 'tyrehandler':
        return tyrehandler_detail(request, id)


def tyrehandler_detail(request, id):
    tyrehandler = TyreHandler.objects.get(id=id)
    return render(request, 'webproduct/tyredetail.html', {'tyrehandler': tyrehandler})


def cylinderhandler_detail(request, id):
    cylinderhandler = CylinderHandler.objects.get(id=id)
    return render(request, 'webproduct/cylinderdetail.html', {'cylinderhandler': cylinderhandler})


def struthandler_detail(request, id):
    struthandler = StrutHandler.objects.get(id=id)
    return render(request, 'webproduct/strutdetail.html', {'struthandler': struthandler})
