from django.db import models
from django.utils.text import slugify

# Create your models here.
class DestinationModel(models.Model):
    destination_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slogan = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='blog_images', blank=True, null=True)
    slug = models.SlugField(default="default")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class RegionModel(models.Model):
    region_id = models.AutoField(primary_key=True)
    destination = models.ForeignKey(DestinationModel, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    image =  models.ImageField(upload_to='blog_images', blank=True, null=True)
    description =  models.TextField()
    is_active = models.BooleanField(default=True)
    is_nav = models.BooleanField(default=False)
    
class TourDetailsModel(models.Model):
    activity_id = models.AutoField(primary_key=True)
    destination = models.ForeignKey(DestinationModel, null=False, on_delete=models.CASCADE)
    region = models.ForeignKey(RegionModel, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    description =  models.TextField()
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
    map = models.URLField(db_index=True, unique=True, blank=True )
    map_overview = models.TextField()
    image =  models.ImageField(upload_to='blog_images', blank=True, null=True)
    is_activity = models.BooleanField(default=False)
    is_attraction = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

class ItinatyModel(models.Model):
    itinary_id = models.AutoField(primary_key=True)
    tour = models.ForeignKey(TourDetailsModel, null= False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False, blank=False)
    day = models.IntegerField(null=False, blank=False )
    start_end = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()

class GallaryModel(models.Model):
    image_id = models.AutoField(primary_key=True)
    tour = models.ForeignKey(TourDetailsModel, null= False, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images', blank=True, null=True)

class IncludeExcludeModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, null=False, blank=False)
    is_include = models.BooleanField(default=True)


class TourIncludeExcludeModel(models.Model):
    id = models.AutoField(primary_key=True)
    tour = models.ForeignKey(TourDetailsModel, on_delete=models.CASCADE)
    sentence = models.ForeignKey(IncludeExcludeModel, on_delete=models.CASCADE)
    is_included = models.BooleanField(default=True)

    class Meta:
        unique_together = ('tour', 'sentence')

class FaqModels(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=250, null=False, blank=False)
    answer = models.TextField()
    is_global = models.BooleanField(default=False)

class TourFaqModels(models.Model):
    id = models.AutoField(primary_key=True)
    tour = models.ForeignKey(TourDetailsModel, on_delete=models.CASCADE)
    question = models.ForeignKey(FaqModels, on_delete=models.CASCADE)
    