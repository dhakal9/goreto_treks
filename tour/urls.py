
from django.urls import path
from .views import AdminDestination, Region, UpdateRegion, DeleteRegion, Destination, UpdateDestination, AdminTour, EditTour, DeleteTour, OneDestination, get_regions, Tourlist, TourDeatails, Activities, Trekking, Itinary, Gallary, DeleteImage
urlpatterns = [
    path('admindestination/', AdminDestination.as_view(), name="admin_destination"),
    path('destination/', Destination.as_view(), name="destination"),
 path('updatedestination/<slug:destination_slug>', UpdateDestination.as_view(), name='update_destination'),
    path('destination/<slug:destination_slug>/', OneDestination.as_view(), name='one_destination'),
    path('adminregion/', Region.as_view(), name="admin_region"),
    path('updateregion/<int:region_id>', UpdateRegion.as_view(), name='update_region'),
    path('deleteregion/<int:region_id>', DeleteRegion.as_view(), name='delete_region'),
    path('admintour/', AdminTour.as_view(), name="admin_tour"),
    path('edit_tour/<int:tour_id>/', EditTour.as_view(), name="edit_tour"),
    path('delete_tour/<int:tour_id>/', DeleteTour.as_view(), name='delete_tour'),
    path('get_regions/',get_regions,name="get_regions"),
    path('tourlist/<int:pk>/', Tourlist.as_view(), name='tour_list'),
    # gauley bhai
    path('tourdetails/<int:pk>/', TourDeatails.as_view(), name='tour_details'),
    path('activities/', Activities.as_view(), name='activities'),
    path('trekking/', Trekking.as_view(), name='trekking'),
    path('itinary/', Itinary.as_view(), name='admin_itinary'),
    path('singlegallary/', Gallary.as_view(), name='admin_gallary'),
    path('delete_single_gallary/<int:image_id>', DeleteImage.as_view(), name='delete_gallary'),
 ]
 