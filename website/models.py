from django.db import models
from ckeditor.fields import RichTextField




class TyreHandler(models.Model):
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
    description = RichTextField(blank=True, null=True)
    price_Toman = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    price_Dollar = models.PositiveSmallIntegerField(null=True, blank=True, default=0)


class CylinderHandler(models.Model):
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
    description = RichTextField(blank=True, null=True)
    price_Toman = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    price_Dollar = models.PositiveSmallIntegerField(null=True, blank=True, default=0)


class StrutHandler(models.Model):
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
    description=RichTextField(blank=True,null=True)
    price_Toman=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    price_Dollar=models.PositiveSmallIntegerField(null=True,blank=True,default=0)



class tyreHandlerImages(models.Model):
    tyreHandler=models.ForeignKey(TyreHandler,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='tyreHandlerImagesProduct/')

class CylinderHandlerImages(models.Model):
    cylinderhandler=models.ForeignKey(CylinderHandler,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='cylinderhandlerImagesProduct/')

class StrutHandlerImages(models.Model):
    struthandler=models.ForeignKey(StrutHandler,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='struthandlerImagesProduct/')



class message(models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    email=models.EmailField()
    title=models.CharField(max_length=20)
    message=models.TextField(max_length=150)

