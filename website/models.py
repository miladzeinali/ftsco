from django.db import models
from ckeditor.fields import RichTextField

class category(models.Model):
    type=models.CharField(max_length=20)
    def __str__(self):
        return self.type

class TyreHandler(models.Model):
    type=models.ForeignKey(category,default=None,on_delete=models.CASCADE)
    name = models.CharField(max_length=15, null=True, blank=True)
    code = models.CharField(max_length=15, null=True, blank=True)
    model_Year = models.CharField(max_length=6, null=True, blank=True)
    capacity_Kg = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    capacity_Lbs = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    OpeningRange_Mm_Min = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    OpeningRange_Mm_Max = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    OpeningRange_In_Min = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    OpeningRange_In_Max = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    sideShift_Mm = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    sideShift_In = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    body_Rotation = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    Pads_Rotation = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    DesignTypeChoice = (
        ('flat', 'flat clamp'),
        ('telescopic', 'telescopic'),
        ('parallelogram', 'parallelogram'),
    )
    Design_Type = models.CharField(max_length=15, choices=DesignTypeChoice, default='flat')
    image = models.ImageField(null=True, blank=True, upload_to='tyrehandler/')
    description=models.TextField(max_length=200,null=True,blank=True)
    price_Toman = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    price_Dollar = models.PositiveSmallIntegerField(null=True, blank=True, default=0)

class CylinderHandler(models.Model):
    type=models.ForeignKey(category,default=None,on_delete=models.CASCADE)
    name = models.CharField(max_length=15, null=True, blank=True)
    code = models.CharField(max_length=15, null=True, blank=True)
    model_Year = models.CharField(max_length=6, null=True, blank=True)
    capacity_Kg = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    capacity_Lbs = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    Cylinder_Diameter_mm_min = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    Cylinder_Diameter_mm_max = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    Cylinder_Diameter_in_min = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    Cylinder_Diameter_in_max = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    sideShift_Mm = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    sideShift_In = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    body_Rotation = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    Handler_tilting = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    image = models.ImageField(null=True, blank=True, upload_to='cylinderhandler/')
    description=models.TextField(max_length=200,null=True,blank=True)
    price_Toman = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    price_Dollar = models.PositiveSmallIntegerField(null=True, blank=True, default=0)

class StrutHandler(models.Model):
    type=models.ForeignKey(category,default=None,on_delete=models.CASCADE)
    name=models.CharField(max_length=15,null=True,blank=True)
    code=models.CharField(max_length=15,null=True,blank=True)
    model_Year=models.CharField(max_length=6,null=True,blank=True)
    capacity_Kg=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    capacity_Lbs=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    Cylinder_Diameter_mm_min=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    Cylinder_Diameter_mm_max=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    Cylinder_Diameter_in_min=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    Cylinder_Diameter_in_max=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    sideShift_Mm=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    sideShift_In=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    body_Rotation=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    Handler_tilting=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    image=models.ImageField(null=True,blank=True,upload_to='struthandler/')
    description=models.TextField(max_length=200,null=True,blank=True)
    price_Toman=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    price_Dollar=models.PositiveSmallIntegerField(null=True,blank=True,default=0)

class BeltHandler(models.Model):
    type=models.ForeignKey(category,default=None,on_delete=models.CASCADE)
    name=models.CharField(max_length=15,null=True,blank=True)
    code=models.CharField(max_length=15,null=True,blank=True)
    model_Year=models.CharField(max_length=6,null=True,blank=True)
    capacity_Kg=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    capacity_Lbs=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    Roll_Diameter_mm=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    Roll_Diameter_in=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    articulation=models.CharField(max_length=5,null=True,blank=True)
    image=models.ImageField(null=True,blank=True,upload_to='belthandler/')
    description=models.TextField(max_length=200,null=True,blank=True)
    price_Toman=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    price_Dollar=models.PositiveSmallIntegerField(null=True,blank=True,default=0)

class Wheelmotor(models.Model):
    type=models.ForeignKey(category,default=None,on_delete=models.CASCADE)
    name=models.CharField(max_length=15,null=True,blank=True)
    code=models.CharField(max_length=15,null=True,blank=True)
    model_Year=models.CharField(max_length=6,null=True,blank=True)
    capacity_Kg=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    capacity_Lbs=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    image=models.ImageField(null=True,blank=True,upload_to='wheelmotor/')
    description=models.TextField(max_length=200,null=True,blank=True)
    price_Toman=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    price_Dollar=models.PositiveSmallIntegerField(null=True,blank=True,default=0)

class PipeHandler(models.Model):
    type = models.ForeignKey(category, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=15, null=True, blank=True)
    code = models.CharField(max_length=15, null=True, blank=True)
    model_Year = models.CharField(max_length=6, null=True, blank=True)
    capacity_Kg = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    capacity_Lbs = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    range_diameter_mm=models.CharField(max_length=5,null=True,blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='wheelmotor/')
    description = models.TextField(max_length=200, null=True, blank=True)
    price_Toman = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    price_Dollar = models.PositiveSmallIntegerField(null=True, blank=True, default=0)

class RodHandler(models.Model):
    type=models.ForeignKey(category,default=None,on_delete=models.CASCADE)
    name = models.CharField(max_length=15, null=True, blank=True)
    code = models.CharField(max_length=15, null=True, blank=True)
    model_Year = models.CharField(max_length=6, null=True, blank=True)
    capacity_Kg=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    capacity_Lbs=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    Cylinder_Diameter_mm_min=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    Cylinder_Diameter_mm_max=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    Cylinder_Diameter_in_min=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    Cylinder_Diameter_in_max=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    range_daimeter=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    image = models.ImageField(null=True, blank=True, upload_to='rodhandler/')
    description = models.TextField(max_length=200, null=True, blank=True)
    price_Toman = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    price_Dollar = models.PositiveSmallIntegerField(null=True, blank=True, default=0)

class CableHandler(models.Model):
    type=models.ForeignKey(category,default=None,on_delete=models.CASCADE)
    name = models.CharField(max_length=15, null=True, blank=True)
    code = models.CharField(max_length=15, null=True, blank=True)
    model_Year = models.CharField(max_length=6, null=True, blank=True)
    capacity_Kg=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    capacity_Lbs=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    Roll_Diameter_mm=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    Roll_Diameter_in=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    image = models.ImageField(null=True, blank=True, upload_to='cablehandler/')
    description = models.TextField(max_length=200, null=True, blank=True)
    price_Toman = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    price_Dollar = models.PositiveSmallIntegerField(null=True, blank=True, default=0)

class tyreHandlerImages(models.Model):
    tyreHandler=models.ForeignKey(TyreHandler,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='tyreHandlerImagesProduct/')

class CylinderHandlerImages(models.Model):
    cylinderhandler=models.ForeignKey(CylinderHandler,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='cylinderhandlerImagesProduct/')

class StrutHandlerImages(models.Model):
    struthandler=models.ForeignKey(StrutHandler,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='struthandlerImagesProduct/')

class BeltHandlerImages(models.Model):
    struthandler=models.ForeignKey(BeltHandler,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='belthandlerImagesProduct/')

class PipeHandlerImages(models.Model):
    struthandler=models.ForeignKey(PipeHandler,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='pipehandlerImagesProduct/')

class WheelmotorImages(models.Model):
    struthandler=models.ForeignKey(Wheelmotor,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='wheelmotorImagesProduct/')

class RodHandlerImages(models.Model):
    rodhandler=models.ForeignKey(RodHandler,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='rodhandlerImagesProduct/')

class CableHandlerImages(models.Model):
    cablehandler=models.ForeignKey(CableHandler,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='cablehandlerImagesProduct/')



class message(models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    email=models.EmailField()
    title=models.CharField(max_length=20)
    message=models.TextField(max_length=150)

class post(models.Model):
    image=models.ImageField(upload_to='post_images')
    title=models.CharField(max_length=50)
    text=models.TextField(max_length=300)


