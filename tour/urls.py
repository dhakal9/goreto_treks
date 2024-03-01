
from django.urls import path
from .views import AdminDestination, Region, Destination, AdminTour, EditTour, OneDestination, get_regions, Tourlist, TourDeatails, Activities, Trekking, Itinary, Gallary
urlpatterns = [
    path('admindestination/', AdminDestination.as_view(), name="admin_destination"),
    path('destination/', Destination.as_view(), name="destination"),
    path('destination/<int:pk>/', OneDestination.as_view(), name='one_destination'),
    path('adminregion/', Region.as_view(), name="admin_region"),
    path('admintour/', AdminTour.as_view(), name="admin_tour"),
    path('edit_tour/<int:tour_id>/', EditTour.as_view(), name="edit_tour"),
    path('get_regions/',get_regions,name="get_regions"),
    path('tourlist/<int:pk>/', Tourlist.as_view(), name='tour_list'),
    # gauley bhai
    path('tourdetails/<int:pk>/', TourDeatails.as_view(), name='tour_details'),
    path('activities/', Activities.as_view(), name='activities'),
    path('trekking/', Trekking.as_view(), name='trekking'),
    path('itinary/', Itinary.as_view(), name='admin_itinary'),
    path('gallary/', Gallary.as_view(), name='admin_gallary'),
 ]
 