
from django.urls import path
from .views import AdminDestination, Region, UpdateRegion, DeleteRegion, ToggleRegionStatus, ToggleSpecialStatus, Destination, UpdateDestination, AdminTour, EditTour, DeleteTour, ToggleAttractionStatus, OneDestination, get_regions, Tourlist, TourDeatails, Activities, Trekking, ItinaryAdmin, get_tour_itineraries, delete_itinerary, DeleteItinary, EditItinary, EditTourItinary, Gallary, DeleteImage, AdminIncludeExclude, DeleteIncludeExclude, EditIncludeExclude, AssignIncludeExcludeView, Faqs, DeleteFaqs, EditFaqs, ToggleFaqsStatus, AssignFaqsToTourView, UnassignFaqsToTourView, GoretoSpecial
from . import views

urlpatterns = [
    path('admindestination/', AdminDestination.as_view(), name="admin_destination"),
    path('destination/', Destination.as_view(), name="destination"),
    path('updatedestination/<int:destination_id>', UpdateDestination.as_view(), name='update_destination'),
#   path('updatedestination/<slug:destination_slug>', UpdateDestination.as_view(), name='update_destination'),
    path('destination/<str:destination_slug>/', OneDestination.as_view(), name='one_destination'),
    path('adminregion/', Region.as_view(), name="admin_region"),
    path('updateregion/<int:region_id>', UpdateRegion.as_view(), name='update_region'),
    path('deleteregion/<int:region_id>', DeleteRegion.as_view(), name='delete_region'),
    path('toggle-region-status/<int:region_id>/', ToggleRegionStatus.as_view(), name='toggle_region_status'),
    path('toggle-special-status/<int:region_id>/', ToggleSpecialStatus.as_view(), name='toggle_special_status'),
    path('admintour/', AdminTour.as_view(), name="admin_tour"),
    path('edit_tour/<int:tour_id>/', EditTour.as_view(), name="edit_tour"),
    path('delete_tour/<int:tour_id>/', DeleteTour.as_view(), name='delete_tour'),
    path('toggle_attraction_status/<int:activity_id>/', ToggleAttractionStatus.as_view(), name='toggle_attraction_status'),
    path('get_regions/',get_regions,name="get_regions"),
    # path('tourlist/<int:pk>/', Tourlist.as_view(), name='tour_list'),
    path('activities/<str:region_slug>/', Tourlist.as_view(), name='tour_list'),
    path('tourdetails/<str:tour_slug>/', TourDeatails.as_view(), name='tour_details'),
    # path('tourdetails/<int:pk>/', TourDeatails.as_view(), name='tour_details'),
    path('activities/', Activities.as_view(), name='activities'),
    path('goretospecial/', GoretoSpecial.as_view(), name='goreto_special'),
    path('trekking/', Trekking.as_view(), name='trekking'),
    path('adminitinary/', ItinaryAdmin.as_view(), name='admin_itinary'),
    path('admin-edit-itinary/<int:itinary_id>/', EditItinary.as_view(), name='edit_itinary'),
    path('delete_itinary/<int:itinary_id>', DeleteItinary.as_view(), name='delete_itinary'),
    path('edit_tour_itinary/<int:activity_id>/', EditTourItinary.as_view(), name='edit_tour_itinary'),
    path('singlegallary/', Gallary.as_view(), name='admin_gallary'),
    path('delete_single_gallary/<int:image_id>', DeleteImage.as_view(), name='delete_gallary'),
    path('admin_include_exclude/', AdminIncludeExclude.as_view(), name="admin_include_exclude"),
    path('delete_include_exclude/<int:id>/', DeleteIncludeExclude.as_view(), name='delete_include_exclude'),
    path('edit_include_exclude/<int:id>/', EditIncludeExclude.as_view(), name='edit_include_exclude'),
    path('assign-include-exclude/<int:tour_id>/', AssignIncludeExcludeView.as_view(), name='assign_include_exclude'),
    path('adminfaq/', Faqs.as_view(), name='admin_faq'),
    path('deletefaqs/<int:id>/', DeleteFaqs.as_view(), name='delete_faq'),
    path('editfaqs/<int:id>/', EditFaqs.as_view(), name='edit_faq'),
    path('changefaqsstatus/<int:id>/', ToggleFaqsStatus.as_view(), name='change_faq'),
    path('assign-faqs-to-tour/<int:tour_id>/', AssignFaqsToTourView.as_view(), name='assign_faqs_to_tour'),
    path('remove-faqs-to-tour/<int:id>/', UnassignFaqsToTourView.as_view(), name='unassign_faqs_to_tour'),
    path('get_tour_itineraries/', get_tour_itineraries, name='get_tour_itineraries'),
    path('delete_itinerary/', delete_itinerary, name='delete_itinerary')
 ]
 # gauley bhai
 #pip uninstall bleach
 #pip install bleach==3.3.1