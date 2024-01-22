
from django.urls import path
from .views import Index, Explore
urlpatterns = [
     path('', Index.as_view(), name="index"),
     path('explore/', Explore.as_view(), name="explore"),
 ]
 