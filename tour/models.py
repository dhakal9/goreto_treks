from django.db import models
from django.utils.text import slugify
from django_summernote.fields import SummernoteTextField
from autoslug import AutoSlugField
# from tinymce.models import HTMLField
from ckeditor.fields import RichTextField

# Create your models here.
class DestinationModel(models.Model):
    destination_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slogan = models.CharField(max_length=255, null=False, blank=False)
    description = RichTextField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='blog_images', blank=True, null=True)
    # slug = models.SlugField(default="default")
    slug = AutoSlugField(populate_from='name', default='', unique=True)

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
    description =  RichTextField()
    is_active = models.BooleanField(default=True)
    is_nav = models.BooleanField(default=False)
    is_special = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='name', default='', unique=True)
    
class TourDetailsModel(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('difficult', 'Difficult'),
    ]

    activity_id = models.AutoField(primary_key=True)
    destination = models.ForeignKey(DestinationModel, null=False, on_delete=models.CASCADE)
    region = models.ForeignKey(RegionModel, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = RichTextField()
    depature = models.CharField(max_length=100, null=True, blank=True)
    start_end = models.CharField(max_length=200, null=True, blank=True)
    max_price = models.CharField(max_length=200, null=True, blank=True)
    price = models.CharField(max_length=200, null=False, blank=False)
    transport = models.CharField(max_length=200, null=True, blank=True)
    season = models.CharField(max_length=200, null=True, blank=True)
    altitude = models.CharField(max_length=200, null=True, blank=True)
    age = models.CharField(max_length=200, null=True, blank=True)
    days = models.CharField(max_length=200, null=True, blank=True)
    map = models.URLField(db_index=True, unique=True, blank=True, max_length=2048)
    map_overview = RichTextField()
    image = models.ImageField(upload_to='blog_images', blank=False, null=True)
    is_activity = models.BooleanField(default=False)
    is_attraction = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    slug = AutoSlugField(populate_from='name', default='', unique=True)
    difficulty_level = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='moderate')
    itinary_pdf = models.FileField(upload_to='documents', null=True, blank=True)
    total_reviews = models.CharField(max_length=200, null=True, blank=True, default='79')
    star_rating = models.CharField(max_length=200, null=True, blank=True,default='5' )
    price_1 = models.CharField(max_length=200, null=True, blank=True, default='20$')
    price_2 = models.CharField(max_length=200, null=True, blank=True, default='20$')
    price_35 = models.CharField(max_length=200, null=True, blank=True, default='20$')
    price_510 = models.CharField(max_length=200, null=True, blank=True, default='20$')
    
    def __str__(self):
        return self.name

class ItinatyModel(models.Model):
    itinary_id = models.AutoField(primary_key=True)
    tour = models.ForeignKey(TourDetailsModel, null= False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    day = models.CharField(max_length=8, null=True, blank=True )
    # start_end = models.CharField(max_length=200, null=True, blank=True)
    description = RichTextField()

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
    answer = RichTextField()
    is_global = models.BooleanField(default=False)

class TourFaqModels(models.Model):
    id = models.AutoField(primary_key=True)
    tour = models.ForeignKey(TourDetailsModel, on_delete=models.CASCADE)
    question = models.ForeignKey(FaqModels, on_delete=models.CASCADE)
    
class SpecialModels(models.Model):
    id = models.AutoField(primary_key=True)
    trekking_des = RichTextField()
    goreto_special_des = RichTextField()
    
class FeaturedTourModels(models.Model):
    id = models.AutoField(primary_key=True)
    tour = models.ForeignKey(TourDetailsModel, on_delete=models.CASCADE)
    starting_date = models.DateField()
    end_date = models.DateField()
    