
from django.urls import path
from .views import Destination
urlpatterns = [
     path('admindestination/', Destination.as_view(), name="admin_destination"),
     
 ]
 