
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserLoginForm, CompanyProfileForm, ReviewForm, FunfactForm
from django.contrib.auth import login, authenticate
from .models import CustomUser, CompanyProfile, Review, FunfactModel
from tour.models import DestinationModel
from django.contrib import messages

# Create your views here.

class Index(View):
    template_name = "index.html"
    def get(self,request):
        company_profile = CompanyProfile.objects.first()
        reviews =  Review.objects.all()
        destinations = DestinationModel.objects.all()
        funfact = FunfactModel.objects.first()
        return render(request, self.template_name, {'company': company_profile, 'reviews': reviews, 'funfact':funfact, 'destinations': destinations})
    
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
            return redirect('/')
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
                    return redirect("index")
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
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_review')  # Redirect to a success page or another view

        return render(request, self.template_name, {'form': form})

