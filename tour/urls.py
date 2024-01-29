
from django.urls import path
from .views import AdminDestination, Region, Destination, AdminTour, OneDestination,get_regions
urlpatterns = [
    path('admindestination/', AdminDestination.as_view(), name="admin_destination"),
    path('destination/', Destination.as_view(), name="destination"),
    path('destination/<int:pk>/', OneDestination.as_view(), name='one_destination'),
    path('adminregion/', Region.as_view(), name="admin_region"),
    path('admintour/', AdminTour.as_view(), name="admin_tour"),
    path('get_regions/',get_regions,name="get_regions")
 ]
 