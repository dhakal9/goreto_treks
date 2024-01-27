from django.db import models

# Create your models here.
class DestinationModel(models.Model):
    destinati_id =  models.AutoField(primary_key=True)
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
    
class ActivitiesModel(models.Model):
    actvity_id = models.AutoField(primary_key=True)
    region = models.ForeignKey(RegionModel, null=False, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=100, null=False, blank=False)
    is_activity = models.BooleanField(default=False)
    is_acttraction = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    activity_image =  models.ImageField(upload_to='blog_images', blank=True, null=True)
    discription =  models.TextField(max_length=2000)

