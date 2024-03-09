# models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True) 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Add related_name to avoid clashes with the default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        related_query_name='user',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        related_query_name='user',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.email


class CompanyProfile(models.Model):
    name  = models.CharField(max_length=300, null=False, blank=False)
    email = models.EmailField(unique=True, max_length=255 )
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length = 15)
    slogan1 = models.CharField(max_length = 200)
    slogan2 = models.CharField(max_length = 200)
    about_sub_heading = models.CharField(max_length = 200)
    about_heading = models.CharField(max_length = 200)
    about_thumbnail = models.ImageField(upload_to='company_images', blank=True, null=True)
    about_us = models.TextField()
    home_image = models.ImageField(upload_to='company_images', blank=True, null=True)
    banner1_image = models.ImageField(upload_to='company_images', blank=True, null=True)
    banner2_image = models.ImageField(upload_to='company_images', blank=True, null=True)
    logo_image =  models.ImageField(upload_to='company_images', blank=True, null=True)
    video_thumbnail_image = models.ImageField(upload_to='company_images', blank=True, null=True)
    video_link = models.URLField(max_length=128, db_index=True, unique=True, blank=True )
    # video_link = models.URLField(("Trip Number"), max_length=128, db_index=True, unique=True, blank=True )
    
class Funfacts(models.Model):
   funfact_id =  models.AutoField(primary_key=True) 
   name = models.CharField(max_length = 200)
   discription = models.CharField(max_length = 200) 
   
class ExcludeInclude(models.Model):
    funfact_id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length = 200) 
    is_active = models.BooleanField(default=True)
    
class OurTeamModel(models.Model):
    team_id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length = 200) 
    position = models.CharField(max_length = 200)
    team_image =  models.ImageField(upload_to='blog_images', blank=True, null=True)
    facebook_link = models.URLField(max_length=128, db_index=True, unique=True, blank=True )
    instagram_link = models.URLField(max_length=128, db_index=True, unique=True, blank=True )
    is_active = models.BooleanField(default=True)
    
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    team_image =  models.ImageField(upload_to='blog_images', blank=True, null=True)
    name = models.CharField(max_length = 200)
    position = models.CharField(max_length = 200)
    message = models.TextField(max_length=500)
    is_active = models.BooleanField(default=True)
    
class FunfactModel(models.Model):
   travellers = models.CharField(max_length = 200)
   places = models.CharField(max_length = 200)
   miles = models.CharField(max_length = 200)
   years = models.CharField(max_length = 200)


class BlogsModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 200, blank=False, null=False)
    description =  models.TextField(max_length=3000, blank=False, null=False)
    image =  models.ImageField(upload_to='blog_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    

class CsrModel(models.Model):
    id = models.AutoField(primary_key=True)
    title =models.CharField(max_length = 200, blank=False, null=False)
    description =  models.TextField(max_length=3000, blank=False, null=False)
    image =  models.ImageField(upload_to='blog_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

class MainGallaryModel(models.Model):
    id = models.AutoField(primary_key=True)
    image =  models.ImageField(upload_to='blog_images', blank=False, null=False)

class WhyUsModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 200, blank=False, null=False)
    description =  models.TextField(max_length=3000, blank=False, null=False)