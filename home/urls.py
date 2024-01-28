
from django.urls import path
from .views import Index, Explore, Login, AdminIndex, AdminHome, Review_function, Funfact, ContactUs, OurTeamAdmin, OurTeam
urlpatterns = [
     path('', Index.as_view(), name="index"),
     path('explore/', Explore.as_view(), name="explore"),
     path('login/', Login.as_view(), name="login"),
     path('adminindex/', AdminIndex.as_view(), name="admin_index"),
     path('adminhome/', AdminHome.as_view(), name="admin_home"),
     path('adminreview/', Review_function.as_view(), name="admin_review"),
     path('adminfunfact/', Funfact.as_view(), name="admin_funfact"),
     path('contact_us/', ContactUs.as_view(), name="contact_us"),
     path('adminteam/', OurTeamAdmin.as_view(), name="admin_team"),
     path('ourteam/', OurTeam.as_view(), name="our_team"),
     
 ]
 