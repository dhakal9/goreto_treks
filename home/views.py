
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserLoginForm, CompanyProfileForm, ReviewForm, FunfactForm, OurTeamForm, ContactUs, BlogsForm, CsrForm, MainGallaryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser, CompanyProfile, Review, FunfactModel, OurTeamModel, BlogsModel, CsrModel, MainGallaryModel
from tour.models import DestinationModel, TourDetailsModel
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

class Index(View):
    template_name = "index.html"
    def get(self,request):
        company_profile = CompanyProfile.objects.first()
        reviews =  Review.objects.all()
        destinations = DestinationModel.objects.all()
        funfact = FunfactModel.objects.first()
        tours = TourDetailsModel.objects.all()
        return render(request, self.template_name, {'company': company_profile, 'reviews': reviews, 'funfact':funfact, 'destinations': destinations, 'tours':tours})
    

    
class Explore(View):
    template_name = "explore.html"
    def get(self, request):
        return render(request, self.template_name)




class Login(View):
    form_name = UserLoginForm
    template_name = 'login.html'
    
    def get(self, request):
        form = self.form_name()
        if request.user.is_authenticated:
            return redirect('admin_home')
        else:
            return render(request, self.template_name, {'form': form})
    
    def post(self, request):
            form = self.form_name(request.POST)
            if form.is_valid():                
                email = request.POST['email']
                password = request.POST['password']
                user = authenticate(request, email=email, password=password)
                # remember_me = request.POST.get("remember_me") == "on"
                if user is not None:
                    # login(request, user)
                    # if remember_me:
                    #     request.session.set_expiry(1209600)
                    #     request.session.set_expiry(0)
                    return redirect("admin_home")
                else:
                    if not CustomUser.objects.filter(email=email).exists():
                        messages.error(request, "Invalid email. Please enter a valid email address.")
                    elif not CustomUser.objects.filter(email=email, password=password).exists():
                        messages.error(request, "Incorrect password. Please enter the correct password.")

            return render(request, self.template_name, {'form': self.form_name})
        

    
class AdminIndex(View):
    template_name = "admin_index.html"
    def get(self, request):
        return render(request, self.template_name)

class AdminHome(View):
    template_name = 'admin_home.html'
    form = CompanyProfileForm

    def get(self, request):
        company_profile = CompanyProfile.objects.first()
        form = self.form(instance=company_profile)  # Pass instance to make it updateable
        return render(request, self.template_name, {'form': form, 'company': company_profile})

    def post(self, request):
        company_profile = CompanyProfile.objects.first()
        form = self.form(request.POST, request.FILES, instance=company_profile)
        if form.is_valid():
            form.save()
            return redirect('admin_home')  # Redirect to the same page after saving

        return render(request, self.template_name, {'form': form})

class Funfact(View):
    template_name = 'admin_funfact.html'
    form = FunfactForm
    
    def get(self, request):
        funfact = FunfactModel.objects.first()
        form = self.form(instance=funfact)  # Pass instance to make it updateable
        return render(request, self.template_name, {'form': form, 'funfact': funfact})
    
    def post(self, request):
        funfact = FunfactModel.objects.first()
        form = self.form(request.POST,  instance=funfact)
        if form.is_valid():
            form.save()
            return redirect('admin_funfact')  # Redirect to the same page after saving

        return render(request, self.template_name, {'form': form, 'funfact': funfact})
    
class Review_function(View):
    template_name = 'admin_review.html'

    def get(self, request):
        form = ReviewForm()
        reviews = Review.objects.all()
        return render(request, self.template_name, {'form': form, 'reviews':reviews})

    def post(self, request):
        reviews = Review.objects.all()
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_review')  # Redirect to a success page or another view

        return render(request, self.template_name, {'form': form, 'reviews':reviews})
    
class DeleteReview(View):
    def get(self, request, review_id):
        reviews = Review.objects.get(review_id=review_id)
        reviews.delete()
        messages.success(request, "Review Deleted Successfully")
        return redirect('admin_review')

class UpdateReview(View):
        def post(self, request, review_id):
            review = Review.objects.get(id=review_id)
            form = ReviewForm(request.POST, request.FILES, instance=review)
            if form.is_valid():
                form.save()
                return redirect('admin_review')
            
class Reviews(View):
    template_name = 'reviews.html'
    def get(self, request):
        reviews = Review.objects.all()
        return render(request, self.template_name, {'reviews':reviews})
        
class ContactUs(View):
    template_name = 'contactus.html'
    def get(self, request):
        form = ContactUs()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = ContactUs()
        if request.method == 'POST':
            message = request.POST['message']
            email = request.POST['email']
            name = request.POST['username']
            phone = request.POST['phone']
            subject = request.POST['subject']

            message_body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"

            send_mail(
                subject,            # Title
                message_body,       # Message
                settings.EMAIL_HOST_USER,  # Sender email
                ['dhakalamrit19@gmail.com'],  # Receiver email
                fail_silently=False
            )
            messages.success(request, 'Message sent Successfully')
        return render(request, self.template_name, {'form': form})

class OurTeamAdmin(View):
    template_name = 'admin_team.html'
    def get(self, request):
        form = OurTeamForm()
        teams = OurTeamModel.objects.all()
        return render( request, self.template_name, {'form':form, 'teams':teams})
    
    def post(self, request):
        teams = OurTeamModel.objects.all()
        form = OurTeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_team')  # Redirect to a success page or another view

        return render(request, self.template_name, {'form': form, 'teams':teams})

class OurTeam(View):
    template_name='our_team.html'
    def get(self, request):
        teams = OurTeamModel.objects.all()
        return render(request, self.template_name, {'teams':teams})
    
class OurTeamDetails(View):
    template_name = 'our_team_details.html'
    def get(self, request):
        teams = OurTeamModel.objects.all()
        return render(request, self.template_name, {'teams':teams})
    
class Logout(LoginRequiredMixin, View):
    template_name = 'login.html'
    def get(self, request):
        logout(request)
        return redirect('login')

class AdminBlogs(View):
    template_name = 'admin_blogs.html'
    def get(self, request):
        blogs = BlogsModel.objects.all()
        form = BlogsForm()
        return render(request, self.template_name, {'form':form, 'blogs':blogs})
    
    def post(self, request):
        form = BlogsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blogs Added Successfully')
            return redirect('admin_blogs')
        return render(request, self.template_name, {'form':form})
    
class Blogs(View):
    template_name = 'blogs.html'
    def get(self, request):
        blogs = BlogsModel.objects.all()
        return render(request, self.template_name, {'blogs':blogs})

class BlogsDetails(View):
    template_name = 'blogs_details.html'
    def get(self, request, pk):
        blogs = BlogsModel.objects.get(pk=pk)
        return render(request, self.template_name, {'blogs':blogs})

class AboutUs(View):
    template_name = 'aboutus.html'
    def get(self, request):
        teams = OurTeamModel.objects.all()
        reviews =  Review.objects.all()
        return render(request, self.template_name, {'teams':teams, 'reviews':reviews})
    

class WhyUs(View):
    template_name ='why_us.html'
    def get(self, request):
        return render(request, self.template_name)
    

class CsrAdmin(View):
    template_name = 'admin_csr.html'
    def get(self, request):
        csrs = CsrModel.objects.all()
        form = CsrForm()
        return render(request, self.template_name, {'form':form, 'csrs':csrs})
    
    def post(self, request):
        csrs = CsrModel.objects.all()
        form = CsrForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'CSR Added successfully')
            return redirect('csr_admin')
        return render(request, self.template_name, {'form':form, 'csrs':csrs})
    
class Csr(View):
    template_name = 'csr.html'
    def get(self, request):
        csrs = CsrModel.objects.all()
        return render(request, self.template_name, {'csrs':csrs})
    
class CsrDetails(View):
    template_name = 'csr_details.html'
    def get(self, request, pk):
        csrs = CsrModel.objects.get(pk=pk)
        return render(request, self.template_name, {'csrs':csrs})
    
class MainGallaryAdmin(View):
    template_name = 'admin_main_gallary.html'
    def get(self, request):
        form = MainGallaryForm()
        images = MainGallaryModel.objects.all()
        return render(request, self.template_name, {'form':form, 'images':images})
    def post(self, request):
        images = MainGallaryModel.objects.all()
        form = MainGallaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image Added successfully')
            return redirect('main_admin_gallary')
        return render(request, self.template_name, {'form':form, 'images':images})
    
class Gallary(View):
    tempale_name = 'gallary.html'
    def get(self, request):
        images = MainGallaryModel.objects.all()
        return render(request, self.tempale_name, {'images':images})
    