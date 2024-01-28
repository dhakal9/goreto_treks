from django.shortcuts import render, redirect
from django.views import View
from .models import DestinationModel, RegionModel, TourDetailsModel, ItinatyModel
from .forms import DestinationForm, RegionForm, TourDetailsForm, ItinatyForm

class AdminDestination(View):
    template_name = "admin_destination.html"
    form_class = DestinationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_destination')  # Replace 'your_redirect_url' with the actual URL to redirect after form submission

        return render(request, self.template_name, {'form': form})

class Destination(View):
    template_name = "destination.html"
    def get(self, request):
        return render(request, self.template_name) 
    
class OneDestination(View):
    template_name = 'one_destination.html'

    def get(self, request, pk):
        countries = DestinationModel.objects.get(pk=pk)
        return render(request, self.template_name, {'contries': countries})

        
class Region(View):
    template_name = "admin_region.html"
    form_class = RegionForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            region_instance = form.save()
            return redirect('admin_region')

        return render(request, self.template_name, {'form': form})
    
class AdminTour(View):
    template_name = 'admin_tour.html'

    def get(self, request):
        form = TourDetailsForm()
        form1 = ItinatyForm()
        return render(request, self.template_name, {'form': form, 'form1':form1})

    def post(self, request):
        form1 = ItinatyForm()
        form = TourDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_tour')  # Replace 'your_redirect_url' with the actual URL to redirect after form submission

        return render(request, self.template_name, {'form': form, 'form1':form1})

