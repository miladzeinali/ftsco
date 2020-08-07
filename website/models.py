from django.db import models

class TyreHandler(models.Model):
    name=models.TextField(max_length=15,null=True,blank=True)
    code=models.TextField(max_length=15,null=True,blank=True)
    modelYear=models.TextField(max_length=15,null=True,blank=True)
    capacityKg=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    capacityLbs=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    OpeningRangeMmMin=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    OpeningRangeMmMax=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    OpeningRangeInMin=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    OpeningRangeInMax=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    sideShiftMm=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    sideShiftIn=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    bodyRotation=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    PadsRotation=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    DesignTypeChoice=(
        ('flat','flat clamp'),
        ('telescopic','telescopic'),
        ('parallelogram','parallelogram'),
    )
    DesignType=models.TextField(max_length=15,default='flat')
    image=models.ImageField(null=True,blank=True,upload_to='tyrehandler/')
    description=models.TextField(max_length=50,null=True,blank=True)
    priceToman=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    priceDollar=models.PositiveSmallIntegerField(null=True,blank=True,default=0)
