from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import DestinationModel, RegionModel, TourDetailsModel, ItinatyModel, GallaryModel
from .forms import DestinationForm, RegionForm, TourDetailsForm, ItinaryForm, GallaryForm
from django.contrib import messages

def get_regions(request):
    destination_id = request.GET.get('destination_id')
    regions = RegionModel.objects.filter(destination_id=destination_id).values('region_id', 'name')
    return JsonResponse({'regions': list(regions)})

class AdminDestination(View):
    template_name = "admin_destination.html"
    form_class = DestinationForm

    def get(self, request):
        destinations = DestinationModel.objects.all()
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'destinations': destinations})

    def post(self, request):
        destinations = DestinationModel.objects.all()
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_destination')  # Replace 'your_redirect_url' with the actual URL to redirect after form submission

        return render(request, self.template_name, {'form': form, 'destinations': destinations})

class Destination(View):
    template_name = "destination.html"
    def get(self, request):
        return render(request, self.template_name) 
    
class OneDestination(View):
    template_name = 'one_destination.html'

    def get(self, request, pk):
        countries = DestinationModel.objects.get(pk=pk)
        regions = RegionModel.objects.all()
        return render(request, self.template_name, {'country': countries, 'regions':regions})

        
class Region(View):
    template_name = "admin_region.html"
    form_class = RegionForm

    def get(self, request):
        regions = RegionModel.objects.all()
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'regions':regions})

    def post(self, request):
        regions = RegionModel.objects.all()
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            region_instance = form.save()
            return redirect('admin_region')

        return render(request, self.template_name, {'form': form, 'regions':regions})
    

    
class Tourlist(View):
    template_name = 'tourlist.html'
    def get(self, request, pk):
        region = RegionModel.objects.get(pk=pk)
        print(pk)
        tours = TourDetailsModel.objects.all()
        return render(request, self.template_name, {'region':region, 'tours':tours})
        
class AdminTour(View):
    template_name = 'admin_tour.html'

    def get(self, request):
        form = TourDetailsForm()
        form1 = ItinaryForm()
        tours = TourDetailsModel.objects.all()
        return render(request, self.template_name, {'form': form, 'form1':form1, 'tours':tours})

    def post(self, request):
        tours = TourDetailsModel.objects.all()
        form1 = ItinaryForm(request.POST, request.FILES)
        form = TourDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_tour')
        
        return render(request, self.template_name, {'form': form, 'form1':form1, 'tours':tours})
    
class EditTour(View):
    template_name = 'admin_tour.html'

    def get(self, request, tour_id):
        tour = get_object_or_404(TourDetailsModel, pk=tour_id)
        form = TourDetailsForm(instance=tour)
        form1 = ItinaryForm()
        tours = TourDetailsModel.objects.all()
        return render(request, self.template_name, {'form': form, 'form1':form1, 'tours':tours})

    def post(self, request, tour_id):
        tour = get_object_or_404(TourDetailsModel, pk=tour_id)
        form1 = ItinaryForm(request.POST, request.FILES)
        form = TourDetailsForm(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            form.save()
            return redirect('admin_tour')
        
        return render(request, self.template_name, {'form': form, 'form1':form1, 'tours':tours})


class TourDeatails(View):
    template_name = 'tour_details.html'
    def get(self, request, pk):
        tour_details = TourDetailsModel.objects.get(pk=pk)
        images = GallaryModel.objects.all()
        return render(request, self.template_name, {'tour_details':tour_details, 'images':images})

class Itinary(View):
    template_name ='admin_itinary.html'
    def get(self, request):
        form = ItinaryForm()
        itinaries = ItinatyModel.objects.all()
        tours = TourDetailsModel.objects.all()
        return render(request, self.template_name, {'form': form, 'tours':tours, 'itinaries':itinaries})
    
    def post(self, request):
        itinaries = ItinatyModel.objects.all()
        tours = TourDetailsModel.objects.all()
        form = ItinaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Itinary saved Successfully')
            return redirect('admin_itinary') # Replace 'your_redirect_url' with the actual URL to redirect after form submission
        return render(request, self.template_name, {'form': form, 'tours':tours, 'itinaries':itinaries})
    
class Gallary(View):
    template_name ='admin_gallary.html'
    def get(self, request):
        form = GallaryForm()
        images = GallaryModel.objects.all()
        tours = TourDetailsModel.objects.all()
        return render(request, self.template_name, {'form': form, 'tours':tours, 'images':images})
    
    def post(self, request):
        tours = TourDetailsModel.objects.all()
        images = GallaryModel.objects.all()
        form = GallaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image Added Successfully')
            return redirect('admin_gallary') # Replace 'your_redirect_url' with the actual URL to redirect after form submission
        return render(request, self.template_name, {'form': form, 'tours':tours, 'images':images})


class Activities(View):
    template_name = 'activities.html'
    def get(self, request):
        return render(request, self.template_name)

class Trekking(View):
    template_name ='trekking.html'
    def get(self, request):
        return render(request, self.template_name)