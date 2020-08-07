from django.db import models

class TyreHandler(models.Model):
    name=models.CharField(max_length=15,null=True,blank=True)
    code=models.CharField(max_length=15,null=True,blank=True)
    model_Year=models.CharField(max_length=6,null=True,blank=True)
    capacity_Kg=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    capacity_Lbs=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    OpeningRange_Mm_Min=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    OpeningRange_Mm_Max=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    OpeningRange_In_Min=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    OpeningRange_In_Max=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    sideShift_Mm=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    sideShift_In=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    bodyRotation=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    PadsRotation=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    DesignTypeChoice=(
        ('flat','flat clamp'),
        ('telescopic','telescopic'),
        ('parallelogram','parallelogram'),
    )
    DesignType=models.CharField(max_length=15,choices=DesignTypeChoice,default='flat')
    image=models.ImageField(null=True,blank=True,upload_to='tyrehandler/')
    description=models.CharField(max_length=50,null=True,blank=True)
    priceToman=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    priceDollar=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
