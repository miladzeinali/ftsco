from django.shortcuts import render,redirect
from .models import TyreHandler, CylinderHandler, StrutHandler,message,post,BeltHandler,Wheelmotor,PipeHandler


# Create your views here.


def home(request):
    return render(request, 'pages/home.html', {})

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

def pipehandler(request):
    pipehandler = PipeHandler.objects.all()
    count = len(pipehandler)
    return render(request, 'webproduct/listproduct.html', {'products': pipehandler, 'count': count})

def wheelmotor(request):
    wheelmotor = Wheelmotor.objects.all()
    count = len(wheelmotor)
    return render(request, 'webproduct/listproduct.html', {'products': wheelmotor, 'count': count})

def belthandler(request):
    belthandler = BeltHandler.objects.all()
    count = len(belthandler)
    return render(request, 'webproduct/listproduct.html', {'products': belthandler, 'count': count})

def productcontrol(request, id, type):
    if type == 'cylinderhandler':
        return cylinderhandler_detail(request, id)
    elif type == 'struthandler':
        return struthandler_detail(request, id)
    elif type == 'tyrehandler':
        return tyrehandler_detail(request, id)
    elif type == 'belthandler':
        return belthandler_detail(request, id)
    elif type == 'wheelmotor':
        return wheelmotor_detail(request, id)
    elif type == 'pipehandler':
        return pipehandler_detail(request, id)

def tyrehandler_detail(request, id):
    tyrehandler = TyreHandler.objects.get(id=id)
    return render(request, 'webproduct/tyredetail.html', {'tyrehandler': tyrehandler})

def cylinderhandler_detail(request, id):
    cylinderhandler = CylinderHandler.objects.get(id=id)
    return render(request, 'webproduct/cylinderdetail.html', {'cylinderhandler': cylinderhandler})

def struthandler_detail(request, id):
    struthandler = StrutHandler.objects.get(id=id)
    return render(request, 'webproduct/strutdetail.html', {'struthandler': struthandler})

def belthandler_detail(request, id):
    belthandler = BeltHandler.objects.get(id=id)
    return render(request, 'webproduct/beltdetail.html', {'belthandler': belthandler})

def wheelmotor_detail(request, id):
    wheelmotor = Wheelmotor.objects.get(id=id)
    return render(request, 'webproduct/wheeldetail.html', {'wheelmotor': wheelmotor})

def pipehandler_detail(request, id):
    pipehandler = PipeHandler.objects.get(id=id)
    return render(request, 'webproduct/pipedetail.html', {'pipehandler': pipehandler})



def contact(request):
    return render(request,'pages/contact.html',{})

def messages(request):
    print(request.POST)
    name=request.POST['name']
    email=request.POST['email']
    subject=request.POST['subject']
    messages=request.POST['message']
    phone=request.POST['phone']
    message.objects.create(name=name,email=email,message=messages,title=subject,phone=phone)
    return redirect('website:home')

def about(request):
    return render(request,'pages/about.html',{})

def history(request):
    posts=post.objects.all()
    return render(request,'pages/posts.html',{'posts':posts})