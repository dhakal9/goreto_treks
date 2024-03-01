
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .views import Index, Explore, Login, Logout, AdminIndex, AdminHome, Review_function, Reviews, DeleteReview, UpdateReview, Funfact, ContactUs, OurTeamAdmin, OurTeam, OurTeamDetails, AdminBlogs, Blogs, BlogsDetails, AboutUs, WhyUs, CsrAdmin, Csr, CsrDetails
urlpatterns = [
     path('', Index.as_view(), name="index"),
     path('explore/', Explore.as_view(), name="explore"),
     path('login/', Login.as_view(), name="login"),
     path("logout/", Logout.as_view(), name="logout"),
     path('adminindex/', AdminIndex.as_view(), name="admin_index"),
     path('adminhome/', AdminHome.as_view(), name="admin_home"),
     path('adminreview/', Review_function.as_view(), name="admin_review"),
     path('deletereview/<int:review_id>', DeleteReview.as_view(), name='delete_review'),
     path('updatereview/<int:review_id>', UpdateReview.as_view(), name='update_review'),
     path('adminfunfact/', Funfact.as_view(), name="admin_funfact"),
     path('contact_us/', ContactUs.as_view(), name="contact_us"),
     path('adminteam/', OurTeamAdmin.as_view(), name="admin_team"),
     path('ourteam/', OurTeam.as_view(), name="our_team"),
     path('ourteamdetails/', OurTeamDetails.as_view(), name="our_team_details"),
     path('adminblogs/', AdminBlogs.as_view(), name="admin_blogs"),
     path('blogs/', Blogs.as_view(), name="blogs"),
     path('blogs/<int:pk>', BlogsDetails.as_view(), name="blogs_details"),
     path('aboutus/', AboutUs.as_view(), name="about_us"),
     path('whyus/', WhyUs.as_view(), name="why_us"),
     path('csradmin/', CsrAdmin.as_view(), name="csr_admin"),
     path('csr/', Csr.as_view(), name="csr"),
     path('csr/<int:pk>', CsrDetails.as_view(), name="csr_details"),
     path('reviews/', Reviews.as_view(), name='reviews')
     
 ]
 