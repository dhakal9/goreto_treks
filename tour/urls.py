
from django.urls import path
from .views import AdminDestination, Region, Destination
urlpatterns = [
    path('admindestination/', AdminDestination.as_view(), name="admin_destination"),
    path('destination/', Destination.as_view(), name="destination"),
    path('adminregion/', Region.as_view(), name="admin_region"),
 ]
 