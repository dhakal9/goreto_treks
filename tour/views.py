from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import DestinationModel, RegionModel, TourDetailsModel, ItinatyModel, GallaryModel, IncludeExcludeModel
from .forms import DestinationForm, RegionForm, TourDetailsForm, ItinaryForm, GallaryForm, BookingForm, InqueryForm, IncludeExcludeForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

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

class UpdateDestination(View):
    template_name = 'admin_destination.html'

    def get(self, request, destination_id):
        destinations = DestinationModel.objects.all()
        destination = get_object_or_404(DestinationModel, destination_id=destination_id)
        form = DestinationForm(instance=destination)
        return render(request, self.template_name, {'form': form, 'destination': destination, 'destinations': destinations})

    def post(self, request, destination_id):
        destination = get_object_or_404(DestinationModel, destination_id=destination_id)
        form = DestinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            messages.success(request, 'Destination Updated Successfully')
            return redirect('admin_destination')
        return render(request, self.template_name, {'form': form, 'destination': destination})

class Destination(View):
    template_name = "destination.html"
    def get(self, request):
        return render(request, self.template_name) 
    
class OneDestination(View):
    template_name = 'one_destination.html'

    def get(self, request, destination_id):
        countries = DestinationModel.objects.get(destination_id=destination_id)
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
    
class UpdateRegion(View):
    template_name = 'admin_region.html'
    def get(self, request, region_id):
        regions = RegionModel.objects.all()
        region= get_object_or_404(RegionModel, pk=region_id)
        form = RegionForm(instance=region)
        return render(request, self.template_name, {'form': form, 'region':region, 'regions':regions })

    def post(self, request, region_id):
        region = get_object_or_404(RegionModel, pk=region_id)
        form = RegionForm(request.POST, request.FILES, instance=region)
        if form.is_valid():
            form.save()
            messages.success(request, 'Region Updated Successfully')
            return redirect('admin_region')
        return render(request, self.template_name, {'form': form,  'region':region})

class DeleteRegion(View):
    def get(self, request, region_id):
        regions = RegionModel.objects.get(region_id=region_id)
        regions.delete()
        messages.success(request, "Region Deleted Successfully")
        return redirect('admin_region')
    

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
        tours = TourDetailsModel.objects.all()
        return render(request, self.template_name, {'form': form, 'tours':tours})

    def post(self, request):
        tours = TourDetailsModel.objects.all()
        form = TourDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_tour')
        
        return render(request, self.template_name, {'form': form, 'tours':tours})
    
class EditTour(View):
    template_name = 'admin_tour.html'

    def get(self, request, tour_id):
        tour = get_object_or_404(TourDetailsModel, pk=tour_id)
        form = TourDetailsForm(instance=tour)
        tours = TourDetailsModel.objects.all()
        return render(request, self.template_name, {'form': form, 'tours':tours})

    def post(self, request, tour_id):
        tour = get_object_or_404(TourDetailsModel, pk=tour_id)
        form = TourDetailsForm(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            form.save()
            return redirect('admin_tour')
        return render(request, self.template_name, {'form': form,  'tour':tour})

class DeleteTour(View):
    def get(self, request, tour_id):
        tours = TourDetailsModel.objects.get(pk=tour_id)
        tours.delete()
        messages.success(request, "Tour Deleted Successfully")
        return redirect('admin_tour')
    
class TourDeatails(View):
    template_name = 'tour_details.html'

    def get(self, request, pk):
        inquiry_form = InqueryForm()
        booking_form = BookingForm()
        tour_details = TourDetailsModel.objects.get(pk=pk)
        images = GallaryModel.objects.all()
        itinaries = ItinatyModel.objects.all()
        return render(request, self.template_name, {'tour_details': tour_details, 'images': images, 'itinaries': itinaries, 'booking_form': booking_form, 'inquiry_form': inquiry_form})

    def post(self, request, pk):
        tour_details = TourDetailsModel.objects.get(pk=pk)
        images = GallaryModel.objects.all()
        itinaries = ItinatyModel.objects.all()

        if request.method == 'POST':
            if 'booking_form_submit' in request.POST:
                booking_form = BookingForm(request.POST)
                if booking_form.is_valid():
                    name = booking_form.cleaned_data['username']
                    email = booking_form.cleaned_data['email']
                    phone = booking_form.cleaned_data['phone']
                    message = booking_form.cleaned_data['message']
                    subject = "Booking Inquiry"

                    message_body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"

                    send_mail(
                        subject,  # Title
                        message_body,  # Message
                        settings.EMAIL_HOST_USER,  # Sender email
                        ['dhakalamrit19@gmail.com'],  # Receiver email
                        fail_silently=False
                    )
                    messages.success(request, 'Booking Inquiry sent Successfully')
                    return redirect('tour_details', pk=pk)  # Redirect to a success URL after form submission

            elif 'inquiry_form_submit' in request.POST:
                inquiry_form = InqueryForm(request.POST)
                if inquiry_form.is_valid():
                    name = inquiry_form.cleaned_data['username']
                    email = inquiry_form.cleaned_data['email']
                    message = inquiry_form.cleaned_data['message']
                    subject = "General Inquiry"

                    message_body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

                    send_mail(
                        subject,  # Title
                        message_body,  # Message
                        settings.EMAIL_HOST_USER,  # Sender email
                        ['dhakalamrit19@gmail.com'],  # Receiver email
                        fail_silently=False
                    )
                    messages.success(request, 'General Inquiry sent Successfully')
                    return redirect('tour_details', pk=pk)  # Redirect to a success URL after form submission

        # If neither booking nor inquiry form is submitted, render the template with the forms
        booking_form = BookingForm()
        inquiry_form = InqueryForm()
        return render(request, self.template_name, {'tour_details': tour_details, 'images': images, 'itinaries': itinaries, 'booking_form': booking_form, 'inquiry_form': inquiry_form})


class ItinaryAdmin(View):
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

class EditItinary(View):
    template_name = 'admin_itinary.html'

    def get(self, request, itinary_id):
        itinaries = ItinatyModel.objects.all()
        itinary = get_object_or_404(ItinatyModel, pk=itinary_id)
        form = ItinaryForm(instance=itinary)
        tours = TourDetailsModel.objects.all()
        return render(request, self.template_name, {'form': form,  'tours':tours, 'itinaries':itinaries})

    def post(self, request, itinary_id):
        itinary = get_object_or_404(ItinatyModel, pk=itinary_id)
        tours = TourDetailsModel.objects.all()
        itinaries = ItinatyModel.objects.all()
        form = ItinaryForm(request.POST, request.FILES, instance=itinary)
        if form.is_valid():
            form.save()
            return redirect('admin_itinary')
        
        return render(request, self.template_name, {'form': form,  'tours':tours, 'itinaries':itinaries})

class DeleteItinary(View):
        def get(self, request, itinary_id):
            itinary = ItinatyModel.objects.get(itinary_id=itinary_id)
            itinary.delete()
            messages.success(request, "Itinary Deleted Successfully")
            return redirect('admin_itinary')
    
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

class DeleteImage(View):
    def get(self, request, image_id):
        images = GallaryModel.objects.get(image_id=image_id)
        images.delete()
        messages.success(request, "Image Deleted Successfully")
        return redirect('admin_gallary')
    
class Activities(View):
    template_name = 'activities.html'
    def get(self, request):
        return render(request, self.template_name)

class Trekking(View):
    template_name ='trekking.html'
    def get(self, request):
        return render(request, self.template_name)

class AdminIncludeExclude(View):
    template_name = 'admin_include_exclude.html'
    def get(self, request):
        details = IncludeExcludeModel.objects.all()
        form = IncludeExcludeForm()
        return render(request, self.template_name, {'form':form, 'details':details})
    
    def post(self, request):
        details = IncludeExcludeModel.objects.all()
        form = IncludeExcludeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Include/Exclude Added Successfully')
            return redirect('admin_include_exclude') # Replace 'your_redirect_url' with the actual URL to redirect after form submission
        return render(request, self.template_name, {'form': form, 'details':details})

class DeleteIncludeExclude(View):
    def get(self, request, id):
        details = IncludeExcludeModel.objects.get(pk=id)
        details.delete()
        messages.success(request, "Include/Exclude Successfully")
        return redirect('admin_include_exclude')

class EditIncludeExclude(View):
    template_name = 'admin_include_exclude.html'

    def get(self, request, id):
        details = IncludeExcludeModel.objects.all()
        det = get_object_or_404(IncludeExcludeModel, pk=id)
        form = IncludeExcludeForm(instance=det)
        return render(request, self.template_name, {'form':form, 'details':details})

    def post(self, request, id):
        det = get_object_or_404(IncludeExcludeModel, pk=id)
        details = IncludeExcludeModel.objects.all()
        form = IncludeExcludeForm(request.POST, instance=det)
        if form.is_valid():
            form.save()
            return redirect('admin_include_exclude')
        return render(request, self.template_name, {'form':form, 'details':details})