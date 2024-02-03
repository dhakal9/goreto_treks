from django.db import models

# Create your models here.
class DestinationModel(models.Model):
    destination_id =  models.AutoField(primary_key=True)
    name = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    slogan = models.CharField(max_length=500, null=False, blank=False)
    description = models.TextField(max_length=10000, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    image =  models.ImageField(upload_to='blog_images', blank=True, null=True)
    
class RegionModel(models.Model):
    region_id = models.AutoField(primary_key=True)
    destination = models.ForeignKey(DestinationModel, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    image =  models.ImageField(upload_to='blog_images', blank=True, null=True)
    description =  models.TextField(max_length=2000)
    is_active = models.BooleanField(default=True)
    is_nav = models.BooleanField(default=False)
    
class TourDetailsModel(models.Model):
    activity_id = models.AutoField(primary_key=True)
    destination = models.ForeignKey(DestinationModel, null=False, on_delete=models.CASCADE)
    region = models.ForeignKey(RegionModel, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    description =  models.TextField(max_length=2000)
    depature = models.CharField(max_length=100, null=True, blank=True)
    time = models.TimeField(null=True)
    start_end = models.CharField(max_length=200, null=True, blank=True)
    max_price = models.CharField(max_length=200, null=True, blank=True)
    price =  models.CharField(max_length=200, null=False, blank=False)
    transport = models.CharField(max_length=200, null=True, blank=True)
    season = models.CharField(max_length=200, null=True, blank=True)
    altitude = models.CharField(max_length=200, null=True, blank=True)
    age = models.CharField(max_length=200, null=True, blank=True)
    days = models.CharField(max_length=200, null=True, blank=True)
    map = models.URLField(max_length=2048, db_index=True, unique=True, blank=True )
    map_overview = models.TextField(max_length=2000)
    image =  models.ImageField(upload_to='blog_images', blank=True, null=True)
    is_activity = models.BooleanField(default=False)
    is_acttraction = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

class ItinatyModel(models.Model):
    itinary_id = models.AutoField(primary_key=True)
    tour = models.ForeignKey(TourDetailsModel, null= False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False, blank=False)
    day = models.IntegerField(null=False, blank=False )
    start_end = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=2000)
    

