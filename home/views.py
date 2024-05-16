
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import UserLoginForm, CompanyProfileForm, ReviewForm, FunfactForm, OurTeamForm, ContactUs, BlogsForm, CsrForm, MainGallaryForm, WhyUsForms, PlanningTripForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser, CompanyProfile, Review, FunfactModel, OurTeamModel, BlogsModel, CsrModel, MainGallaryModel, WhyUsModel
from tour.models import DestinationModel, TourDetailsModel, RegionModel
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.core.serializers import serialize
# Create your views here.

class Index(View):
    template_name = "index.html"
    def get(self,request):
        company_profile = CompanyProfile.objects.first()
        reviews =  Review.objects.all()
        destinations = DestinationModel.objects.all()
        funfact = FunfactModel.objects.first()
        tours = TourDetailsModel.objects.filter(is_attraction=True)
        reg_reg = RegionModel.objects.all()
        
        destinations_json = serialize('json', destinations)
        tours_json = serialize('json', tours)
        regions_json = serialize('json', reg_reg)
        
        return render(request, self.template_name, {'company': company_profile, 'reviews': reviews, 'funfact':funfact, 'destinations': destinations, 'tours':tours, 'destinations_json': destinations_json, 'tours_json': tours_json, 'regions_json': regions_json,})
    

    
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
                    login(request, user)
                    request.session.set_expiry(12090)
                    request.session.set_expiry(0)
                    return redirect("admin_home")
                else:
                    if not CustomUser.objects.filter(email=email).exists():
                        messages.error(request, "Invalid email. Please enter a valid email address.")
                    elif not CustomUser.objects.filter(email=email, password=password).exists():
                        messages.error(request, "Incorrect password. Please enter the correct password.")

            return render(request, self.template_name, {'form': self.form_name})
        

    
class AdminIndex(LoginRequiredMixin, View):
    template_name = "admin_index.html"
    def get(self, request):
        return render(request, self.template_name)

class AdminHome(LoginRequiredMixin, View):
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

class Funfact(LoginRequiredMixin, View):
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
    
class Review_function(LoginRequiredMixin, View):
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
    
class DeleteReview(LoginRequiredMixin, View):
    def get(self, request, review_id):
        reviews = Review.objects.get(review_id=review_id)
        reviews.delete()
        messages.success(request, "Review Deleted Successfully")
        return redirect('admin_review')

class UpdateReview(LoginRequiredMixin, View):
    template_name = 'admin_review.html'

    def get(self, request, review_id):
        reviews = Review.objects.all()
        review = get_object_or_404(Review, pk=review_id)
        form = ReviewForm(instance=review)
        return render(request, self.template_name, {'form': form, 'review':review, 'reviews':reviews })

    def post(self, request, review_id):
        review = get_object_or_404(Review, pk=review_id)
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reviews Updated Successfully')
            return redirect('admin_review')
        return render(request, self.template_name, {'form': form,  'review':review})
            
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
                ['goretotreks@gmail.com'],  # Receiver email
                fail_silently=False
            )
            messages.success(request, 'Message sent Successfully')
        return render(request, self.template_name, {'form': form})

class OurTeamAdmin(LoginRequiredMixin, View):
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
    
class DeleteTeam(LoginRequiredMixin, View):
    def get(self, request, team_id):
        teams = OurTeamModel.objects.get(team_id=team_id)
        teams.delete()
        messages.success(request, "Team Deleted Successfully")
        return redirect('admin_team')
    
class UpdateTeam(LoginRequiredMixin, View):
    template_name = 'admin_team.html'
    def get(self, request, team_id):
        teams = OurTeamModel.objects.all()
        team = get_object_or_404(OurTeamModel, pk=team_id)
        form = OurTeamForm(instance=team)
        return render(request, self.template_name, {'form': form, 'team':team, 'teams':teams })

    def post(self, request, team_id):
        team = get_object_or_404(OurTeamModel, pk=team_id)
        form = OurTeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team Updated Successfully')
            return redirect('admin_team')
        return render(request, self.template_name, {'form': form,  'team':team})

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

class AdminBlogs(LoginRequiredMixin, View):
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
    
class UpdateBlogs(LoginRequiredMixin, View):
    template_name = 'admin_blogs.html'
    def get(self, request, id):
        blogs = BlogsModel.objects.all()
        blog = get_object_or_404(BlogsModel, pk=id)
        form = BlogsForm(instance=blog)
        return render(request, self.template_name, {'form': form, 'blog':blog, 'blogs':blogs })

    def post(self, request, id):
        blog = get_object_or_404(BlogsModel, pk=id)
        form = BlogsForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blogs Updated Successfully')
            return redirect('admin_blogs')
        return render(request, self.template_name, {'form': form,  'blog':blog})

class DeleteBlogs(LoginRequiredMixin, View):
    def get(self, request, id):
        blogs = BlogsModel.objects.get(pk=id)
        blogs.delete()
        messages.success(request, "Blogs Deleted Successfully")
        return redirect('admin_blogs')
    
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
    


class WhyUsAdmin(LoginRequiredMixin, View):
    template_name ='admin_whyus.html'
    def get(self, request):
        form = WhyUsForms() 
        return render(request, self.template_name, {'form':form})

        
    def post(self, request):
        form = WhyUsForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Why Added Successfully')
            return redirect('admin_why_us')
        return render(request, self.template_name, {'form':form})
    
class WhyUs(View):
    template_name ='why_us.html'
    def get(self, request):
        whyuss = WhyUsModel.objects.all()
        return render(request, self.template_name, {'whyuss':whyuss})
    

class CsrAdmin(LoginRequiredMixin, View):
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
    
class UpdateCsr(LoginRequiredMixin, View):
    template_name = 'admin_csr.html'
    def get(self, request, id):
        csrs = CsrModel.objects.all()
        csr = get_object_or_404(CsrModel, pk=id)
        form = CsrForm(instance=csr)
        return render(request, self.template_name, {'form': form, 'csr':csr, 'csrs':csrs })

    def post(self, request, id):
        csr = get_object_or_404(CsrModel, pk=id)
        form = CsrForm(request.POST, request.FILES, instance=csr)
        if form.is_valid():
            form.save()
            messages.success(request, 'CSR Updated Successfully')
            return redirect('csr_admin')
        return render(request, self.template_name, {'form': form,  'csr':csr})

class DeleteCsr(LoginRequiredMixin, View):
    def get(self, request, id):
        csrs = CsrModel.objects.get(pk=id)
        csrs.delete()
        messages.success(request, "CSR Deleted Successfully")
        return redirect('admin_blogs')
    
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
    
class MainGallaryAdmin(LoginRequiredMixin, View):
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
    
class DeleteGallary(LoginRequiredMixin, View):
    def get(self, request, id):
        images = MainGallaryModel.objects.get(id=id)
        images.delete()
        messages.success(request, "Image Deleted Successfully")
        return redirect('main_admin_gallary')

class PlanTrip(View):
    template_name = 'plan_trip.html'  # Replace 'your_template_name.html' with your actual template name

    def get(self, request):
        form = PlanningTripForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PlanningTripForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            tour_name = form.cleaned_data['tour_name']
            address1 = form.cleaned_data['address1']
            address2 = form.cleaned_data['address2']
            city = form.cleaned_data['city']
            zip_code = form.cleaned_data['zip_code']
            state = form.cleaned_data['state']
            country = form.cleaned_data['country']
            message = form.cleaned_data['message']

            message_body = f"First Name: {firstname}\n Last Name: {lastname}\nEmail: {email}\nTour Name: {tour_name}\nAddress 1: {address1}\nAddress 2: {address2}\nCity: {city}\nZip Code: {zip_code}\nState: {state}\nCountry: {country}\nMessage: {message}"

            send_mail(
                "Trip Inquiry",     # Title
                message_body,       # Message
                settings.EMAIL_HOST_USER,  # Sender email
                ['goretotreks@gmail.com'],  # Receiver email
                fail_silently=False
            )
            messages.success(request, 'Message sent successfully')
            return redirect('plan_trip')  # Redirect to a success URL after form submission
        else:
            messages.error(request, 'Failed to send message. Please check the form data.')
            return render(request, self.template_name, {'form': form})