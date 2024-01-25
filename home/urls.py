
from django.urls import path
from .views import Index, Explore, Login, AdminIndex, AdminHome, Review_function, Funfact
urlpatterns = [
     path('', Index.as_view(), name="index"),
     path('explore/', Explore.as_view(), name="explore"),
     path('login/', Login.as_view(), name="login"),
     path('adminindex/', AdminIndex.as_view(), name="admin_index"),
     path('adminhome/', AdminHome.as_view(), name="admin_home"),
     path('adminreview/', Review_function.as_view(), name="admin_review"),
     path('adminfunfact/', Funfact.as_view(), name="admin_funfact"),
 ]
 