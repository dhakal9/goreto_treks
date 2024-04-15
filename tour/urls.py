
from django.urls import path
from .views import AdminDestination, Region, UpdateRegion, DeleteRegion, ToggleRegionStatus, Destination, UpdateDestination, AdminTour, EditTour, DeleteTour, ToggleAttractionStatus, OneDestination, get_regions, Tourlist, TourDeatails, Activities, Trekking, ItinaryAdmin, DeleteItinary, EditItinary, EditTourItinary, Gallary, DeleteImage, AdminIncludeExclude, DeleteIncludeExclude, EditIncludeExclude, AssignIncludeExcludeView
urlpatterns = [
    path('admindestination/', AdminDestination.as_view(), name="admin_destination"),
    path('destination/', Destination.as_view(), name="destination"),
   path('updatedestination/<int:destination_id>', UpdateDestination.as_view(), name='update_destination'),
#  path('updatedestination/<slug:destination_slug>', UpdateDestination.as_view(), name='update_destination'),
    path('destination/<int:destination_id>/', OneDestination.as_view(), name='one_destination'),
    path('adminregion/', Region.as_view(), name="admin_region"),
    path('updateregion/<int:region_id>', UpdateRegion.as_view(), name='update_region'),
    path('deleteregion/<int:region_id>', DeleteRegion.as_view(), name='delete_region'),
    path('toggle-region-status/<int:region_id>/', ToggleRegionStatus.as_view(), name='toggle_region_status'),
    path('admintour/', AdminTour.as_view(), name="admin_tour"),
    path('edit_tour/<int:tour_id>/', EditTour.as_view(), name="edit_tour"),
    path('delete_tour/<int:tour_id>/', DeleteTour.as_view(), name='delete_tour'),
    path('toggle_attraction_status/<int:activity_id>/', ToggleAttractionStatus.as_view(), name='toggle_attraction_status'),
    path('get_regions/',get_regions,name="get_regions"),
    path('tourlist/<int:pk>/', Tourlist.as_view(), name='tour_list'),
    # gauley bhai
    path('tourdetails/<int:pk>/', TourDeatails.as_view(), name='tour_details'),
    path('activities/', Activities.as_view(), name='activities'),
    path('trekking/', Trekking.as_view(), name='trekking'),
    path('itinaryadmin/', ItinaryAdmin.as_view(), name='admin_itinary'),
    path('itinary_edit_admin/<int:itinary_id>/', EditItinary.as_view(), name='edit_itinary'),
    path('delete_itinary/<int:itinary_id>', DeleteItinary.as_view(), name='delete_itinary'),
    path('edit_tour_itinary/<int:activity_id>/', EditTourItinary.as_view(), name='edit_tour_itinary'),
    path('singlegallary/', Gallary.as_view(), name='admin_gallary'),
    path('delete_single_gallary/<int:image_id>', DeleteImage.as_view(), name='delete_gallary'),
    path('admin_include_exclude/', AdminIncludeExclude.as_view(), name="admin_include_exclude"),
    path('delete_include_exclude/<int:id>/', DeleteIncludeExclude.as_view(), name='delete_include_exclude'),
    path('edit_include_exclude/<int:id>/', EditIncludeExclude.as_view(), name='edit_include_exclude'),
    path('assign-include-exclude/<int:tour_id>/', AssignIncludeExcludeView.as_view(), name='assign_include_exclude'),
 ]
 