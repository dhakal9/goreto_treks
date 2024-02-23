
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .views import Index, Explore, Login, Logout, AdminIndex, AdminHome, Review_function, DeleteReview, Funfact, ContactUs, OurTeamAdmin, OurTeam, AdminBlogs, Blogs, AboutUs, WhyUs, CsrAdmin, Csr
urlpatterns = [
     path('', Index.as_view(), name="index"),
     path('explore/', Explore.as_view(), name="explore"),
     path('login/', Login.as_view(), name="login"),
     path("logout/", Logout.as_view(), name="logout"),
     path('adminindex/', AdminIndex.as_view(), name="admin_index"),
     path('adminhome/', AdminHome.as_view(), name="admin_home"),
     path('adminreview/', Review_function.as_view(), name="admin_review"),
      path('deletereview/<int:review_id>', DeleteReview.as_view(), name='delete_review'),
     path('adminfunfact/', Funfact.as_view(), name="admin_funfact"),
     path('contact_us/', ContactUs.as_view(), name="contact_us"),
     path('adminteam/', OurTeamAdmin.as_view(), name="admin_team"),
     path('ourteam/', OurTeam.as_view(), name="our_team"),
     path('adminblogs/', AdminBlogs.as_view(), name="admin_blogs"),
     path('blogs/', Blogs.as_view(), name="blogs"),
     path('aboutus/', AboutUs.as_view(), name="about_us"),
     path('whyus/', WhyUs.as_view(), name="why_us"),
     path('csradmin/', CsrAdmin.as_view(), name="csr_admin"),
     path('csr/', Csr.as_view(), name="csr"),
     
 ]
 