from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import DestinationModel, RegionModel, TourDetailsModel, ItinatyModel, GallaryModel, IncludeExcludeModel, TourIncludeExcludeModel, FaqModels, TourFaqModels
from .forms import DestinationForm, RegionForm, TourDetailsForm, ItinaryForm, GallaryForm, BookingForm, InqueryForm, IncludeExcludeForm, TourIncludeExcludeForm, FaqForm, AssignFaqsToTourForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def get_regions(request):
    destination_id = request.GET.get('destination_id')
    regions = RegionModel.objects.filter(destination_id=destination_id).values('region_id', 'name')
    return JsonResponse({'regions': list(regions)})

class AdminDestination(LoginRequiredMixin, View):
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

class UpdateDestination(LoginRequiredMixin, View):
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

    def get(self, request, destination_slug):
        countries  = get_object_or_404(DestinationModel, slug=destination_slug)
        # countries = DestinationModel.objects.get(name=name)
        regions = RegionModel.objects.all()
        return render(request, self.template_name, {'country': countries, 'regions':regions})

        
class Region(LoginRequiredMixin, View):
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
    
class UpdateRegion(LoginRequiredMixin, View):
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

class DeleteRegion(LoginRequiredMixin, View):
    def get(self, request, region_id):
        regions = RegionModel.objects.get(region_id=region_id)
        regions.delete()
        messages.success(request, "Region Deleted Successfully")
        return redirect('admin_region')

class ToggleRegionStatus(LoginRequiredMixin, View):
    def get(self, request, region_id):
        region = get_object_or_404(RegionModel, pk=region_id)
        region.is_nav = not region.is_nav
        region.save()
        messages.success(request, 'Region status toggled successfully')
        return redirect('admin_region')
    

class ToggleSpecialStatus(LoginRequiredMixin, View):
    def get(self, request, region_id):
        region = get_object_or_404(RegionModel, pk=region_id)
        region.is_special = not region.is_special
        region.save()
        messages.success(request, 'Region status toggled successfully')
        return redirect('admin_region')
    

# class Tourlist(View):
#     template_name = 'tourlist.html'
#     def get(self, request, pk):
#         region = RegionModel.objects.get(pk=pk)
#         tours = TourDetailsModel.objects.all()
#         return render(request, self.template_name, {'region':region, 'tours':tours})

class Tourlist(View):
    template_name = 'tourlist.html'
    
    def get(self, request, region_slug):
        region = get_object_or_404(RegionModel, slug=region_slug)
        tours = TourDetailsModel.objects.all()
        return render(request, self.template_name, {'region': region, 'tours': tours})
        
class AdminTour(LoginRequiredMixin, View):
    template_name = 'admin_tour.html'

    def get(self, request):
        form = TourDetailsForm()
        tours = TourDetailsModel.objects.all()
        return render(request, self.template_name, {'form': form, 'tours': tours})

    def post(self, request):
        tours = TourDetailsModel.objects.all()
        form = TourDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Tour Added Successfully")
            return redirect('admin_tour')
        else:
            # If form is not valid, show error messages
            messages.error(request, "There were errors in the form. Please correct them and submit again.")
        
        return render(request, self.template_name, {'form': form, 'tours': tours})
    
class EditTour(LoginRequiredMixin, View):
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

class DeleteTour(LoginRequiredMixin, View):
    def get(self, request, tour_id):
        tours = TourDetailsModel.objects.get(pk=tour_id)
        tours.delete()
        messages.success(request, "Tour Deleted Successfully")
        return redirect('admin_tour')
    
class ToggleAttractionStatus(LoginRequiredMixin, View):
    def get(self, request, activity_id):
        tour = get_object_or_404(TourDetailsModel, pk=activity_id)
        tour.is_attraction = not tour.is_attraction
        tour.save()
        messages.success(request, 'Attraction status toggled successfully')
        return redirect('admin_tour')

class TourDeatails(View):
    template_name = 'tour_details.html'

    def get(self, request, tour_slug):
        inquiry_form = InqueryForm()
        booking_form = BookingForm()
        tour_details = get_object_or_404(TourDetailsModel, slug=tour_slug)
        images = GallaryModel.objects.all()
        itinaries = ItinatyModel.objects.all()
        inc_excs = TourIncludeExcludeModel.objects.filter(tour=tour_details)
        faqs = TourFaqModels.objects.filter(tour=tour_details)
        similar_trips = TourDetailsModel.objects.filter(region=tour_details.region).exclude(pk=tour_details.pk)
        return render(request, self.template_name, {'tour_details': tour_details, 'images': images, 'itinaries': itinaries, 'booking_form': booking_form, 'inquiry_form': inquiry_form, 'inc_excs':inc_excs, 'faqs':faqs, 'similar_trips':similar_trips})

    def post(self, request, tour_slug):
        tour_details = get_object_or_404(TourDetailsModel, slug=tour_slug)
        images = GallaryModel.objects.all()
        itinaries = ItinatyModel.objects.all()
        inc_excs = TourIncludeExcludeModel.objects.all()
        faqs = TourFaqModels.objects.all()
        similar_trips = TourDetailsModel.objects.filter(region=tour_details.region).exclude(pk=tour_details.pk)
        
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
                        ['goretotreks@gmail.com'],  # Receiver email
                        fail_silently=False
                    )
                    messages.success(request, 'Booking Inquiry sent Successfully')
                    return redirect('tour_details', tour_slug=tour_details.slug)  # Redirect to a success URL after form submission

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
                        ['goretotreks@gmail.com'],  # Receiver email
                        fail_silently=False
                    )
                    messages.success(request, 'General Inquiry sent Successfully')
                    return redirect('tour_details', tour_slug=tour_details.slug)  # Redirect to a success URL after form submission

        # If neither booking nor inquiry form is submitted, render the template with the forms
        booking_form = BookingForm()
        inquiry_form = InqueryForm()
        return render(request, self.template_name, {'tour_details': tour_details, 'images': images, 'itinaries': itinaries, 'booking_form': booking_form, 'inquiry_form': inquiry_form,  'inc_excs':inc_excs, 'faqs':faqs, 'similar_trips':similar_trips})
# class TourDeatails(View):
#     template_name = 'tour_details.html'

#     def get(self, request, pk):
#         inquiry_form = InqueryForm()
#         booking_form = BookingForm()
#         tour_details = TourDetailsModel.objects.get(pk=pk)
#         images = GallaryModel.objects.all()
#         itinaries = ItinatyModel.objects.all()
#         inc_excs = TourIncludeExcludeModel.objects.filter(tour=pk)
#         faqs = TourFaqModels.objects.filter(tour=pk)
#         similar_trips = TourDetailsModel.objects.filter(region=tour_details.region).exclude(pk=pk)
#         return render(request, self.template_name, {'tour_details': tour_details, 'images': images, 'itinaries': itinaries, 'booking_form': booking_form, 'inquiry_form': inquiry_form, 'inc_excs':inc_excs, 'faqs':faqs, 'similar_trips':similar_trips})

#     def post(self, request, pk):
#         tour_details = TourDetailsModel.objects.get(pk=pk)
#         images = GallaryModel.objects.all()
#         itinaries = ItinatyModel.objects.all()
#         inc_excs = TourIncludeExcludeModel.objects.all()
#         faqs = TourFaqModels.objects.all()
#         similar_trips = TourDetailsModel.objects.filter(region=tour_details.region).exclude(pk=pk)
        
#         if request.method == 'POST':
#             if 'booking_form_submit' in request.POST:
#                 booking_form = BookingForm(request.POST)
#                 if booking_form.is_valid():
#                     name = booking_form.cleaned_data['username']
#                     email = booking_form.cleaned_data['email']
#                     phone = booking_form.cleaned_data['phone']
#                     message = booking_form.cleaned_data['message']
#                     subject = "Booking Inquiry"

#                     message_body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"

#                     send_mail(
#                         subject,  # Title
#                         message_body,  # Message
#                         settings.EMAIL_HOST_USER,  # Sender email
#                         ['dhakalamrit19@gmail.com'],  # Receiver email
#                         fail_silently=False
#                     )
#                     messages.success(request, 'Booking Inquiry sent Successfully')
#                     return redirect('tour_details', pk=pk)  # Redirect to a success URL after form submission

#             elif 'inquiry_form_submit' in request.POST:
#                 inquiry_form = InqueryForm(request.POST)
#                 if inquiry_form.is_valid():
#                     name = inquiry_form.cleaned_data['username']
#                     email = inquiry_form.cleaned_data['email']
#                     message = inquiry_form.cleaned_data['message']
#                     subject = "General Inquiry"

#                     message_body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

#                     send_mail(
#                         subject,  # Title
#                         message_body,  # Message
#                         settings.EMAIL_HOST_USER,  # Sender email
#                         ['dhakalamrit19@gmail.com'],  # Receiver email
#                         fail_silently=False
#                     )
#                     messages.success(request, 'General Inquiry sent Successfully')
#                     return redirect('tour_details', pk=pk)  # Redirect to a success URL after form submission

#         # If neither booking nor inquiry form is submitted, render the template with the forms
#         booking_form = BookingForm()
#         inquiry_form = InqueryForm()
#         return render(request, self.template_name, {'tour_details': tour_details, 'images': images, 'itinaries': itinaries, 'booking_form': booking_form, 'inquiry_form': inquiry_form,  'inc_excs':inc_excs, 'faqs':faqs, 'similar_trips':similar_trips})

class ItinaryAdmin(LoginRequiredMixin, View):
    template_name = 'admin_itinary.html'

    def get(self, request):
        form = ItinaryForm()
        tours = TourDetailsModel.objects.all()
        itineraries = ItinatyModel.objects.all()  # Fetch all itineraries to display in the template
        return render(request, self.template_name, {'form': form, 'tours': tours, 'itinaries': itineraries})

    def post(self, request):
        tour_id = request.POST.get("tour")
        tour = TourDetailsModel.objects.get(pk=tour_id)
        
        # Clear existing itineraries for the tour
        ItinatyModel.objects.filter(tour=tour).delete()
        
        # Iterate over the form data to save multiple itineraries
        for key in request.POST:
            if key.startswith("plan_name_"):
                index = key.split("_")[-1]
                name = request.POST.get(f"plan_name_{index}")
                day = request.POST.get(f"day_sequence_{index}")
                description = request.POST.get(f"description_{index}")
                if name and day and description:
                    ItinatyModel.objects.create(tour=tour, name=name, day=day, description=description)
        
        messages.success(request, 'Itinerary saved successfully')
        return redirect('admin_itinary')

@csrf_exempt
def delete_itinerary(request):
    itinary_id = request.POST.get('itinary_id')
    try:
        itinerary = ItinatyModel.objects.get(pk=itinary_id)
        itinerary.delete()
        return JsonResponse({'success': True})
    except ItinatyModel.DoesNotExist:
        return JsonResponse({'error': 'Itinerary not found'}, status=404)

def get_tour_itineraries(request):
    tour_id = request.GET.get('tour_id')
    try:
        tour = TourDetailsModel.objects.get(pk=tour_id)
        itineraries = list(ItinatyModel.objects.filter(tour=tour).values('itinary_id', 'day', 'name', 'description'))
        return JsonResponse({'tour_days': tour.days, 'itineraries': itineraries})
    except TourDetailsModel.DoesNotExist:
        return JsonResponse({'error': 'Tour not found'}, status=404)

class EditItinary(LoginRequiredMixin, View):
    template_name = 'admin_itinary.html'

    def get(self, request, itinary_id):
        itinary = get_object_or_404(ItinatyModel, pk=itinary_id)
        tour = itinary.tour  # Get the tour associated with the itinerary
        itinaries = ItinatyModel.objects.filter(tour=tour)  # Filter itineraries by tour
        form = ItinaryForm(instance=itinary)
        tours = TourDetailsModel.objects.all()
        return render(request, self.template_name, {'form': form, 'tours': tours, 'itinaries': itinaries})
        
    def post(self, request, itinary_id):
        itinary = get_object_or_404(ItinatyModel, pk=itinary_id)
        tour = itinary.tour  # Get the tour associated with the itinerary
        tours = TourDetailsModel.objects.all()
        itinaries = ItinatyModel.objects.filter(tour=tour)  # Filter itineraries by tour
        form = ItinaryForm(request.POST, request.FILES, instance=itinary)
        if form.is_valid():
            form.save()
            # Redirect to the edit_tour_itinary view with the appropriate activity_id
            return redirect(reverse('edit_tour_itinary', kwargs={'activity_id': tour.activity_id}))
        
        return render(request, self.template_name, {'form': form, 'tours': tours, 'itinaries': itinaries})



class DeleteItinary(LoginRequiredMixin, View):
    def get(self, request, itinary_id):
        itinary = get_object_or_404(ItinatyModel, pk=itinary_id)
        tour = itinary.tour  # Get the tour associated with the itinerary
        itinary.delete()
        messages.success(request, "Itinerary Deleted Successfully")
        # Redirect to the edit_tour_itinary view with the appropriate activity_id
        return redirect(reverse('edit_tour_itinary', kwargs={'activity_id': tour.activity_id}))


class EditTourItinary(LoginRequiredMixin, View):
    template_name ='admin_itinary.html'
    
    def get(self, request, activity_id):
        form = ItinaryForm()
        toors = get_object_or_404(TourDetailsModel, activity_id=activity_id)
        tours = TourDetailsModel.objects.all()
        itinaries = ItinatyModel.objects.filter(tour=toors)
        return render(request, self.template_name, {'form': form, 'toors': toors, 'tours': tours, 'itinaries': itinaries})

    def post(self, request, activity_id):
        toors = get_object_or_404(TourDetailsModel, activity_id=activity_id)
        tours = TourDetailsModel.objects.all()
        itinaries = ItinatyModel.objects.filter(tour=toors)
        form = ItinaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Itinary saved Successfully')
            # Redirect with the activity_id parameter
            return redirect(reverse('edit_tour_itinary', kwargs={'activity_id': activity_id}))
        return render(request, self.template_name, {'form': form, 'tours': tours, 'toors': toors, 'itinaries': itinaries})

class Gallary(LoginRequiredMixin, View):
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

class DeleteImage(LoginRequiredMixin, View):
    def get(self, request, image_id):
        images = GallaryModel.objects.get(image_id=image_id)
        images.delete()
        messages.success(request, "Image Deleted Successfully")
        return redirect('admin_gallary')
    
class Activities(View):
    template_name = 'activities.html'
    def get(self, request):
        return render(request, self.template_name)
    

class GoretoSpecial(View):
    template_name="goreto_special.html"
    
    def get(self, request):
        goreto_special = RegionModel.objects.filter(is_special = True)
        return render(request, self.template_name, {'goreto_special': goreto_special})

class Trekking(View):
    template_name = 'trekking.html'
    
    def get(self, request):
        nepali_regions = RegionModel.objects.filter(is_nav=False)
        only_trekkings = TourDetailsModel.objects.filter(region__in=nepali_regions)
        return render(request, self.template_name, {'only_trekkings': only_trekkings})

class AdminIncludeExclude(LoginRequiredMixin, View):
    template_name = 'admin_include_exclude.html'
    def get(self, request):
        tours = TourDetailsModel.objects.all()
        details = IncludeExcludeModel.objects.all()
        form = IncludeExcludeForm()
        return render(request, self.template_name, {'form':form, 'details':details, 'tours':tours})
    
    def post(self, request):
        tours = TourDetailsModel.objects.all()
        details = IncludeExcludeModel.objects.all()
        form = IncludeExcludeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Include/Exclude Added Successfully')
            return redirect('admin_include_exclude') # Replace 'your_redirect_url' with the actual URL to redirect after form submission
        return render(request, self.template_name, {'form': form, 'details':details, 'tours':tours})

class DeleteIncludeExclude(LoginRequiredMixin, View):
    def get(self, request, id):
        details = IncludeExcludeModel.objects.get(pk=id)
        details.delete()
        messages.success(request, "Include/Exclude Successfully")
        return redirect('admin_include_exclude')

class EditIncludeExclude(LoginRequiredMixin, View):
    template_name = 'admin_include_exclude.html'

    def get(self, request, id):
        tours = TourDetailsModel.objects.all()
        details = IncludeExcludeModel.objects.all()
        det = get_object_or_404(IncludeExcludeModel, pk=id)
        form = IncludeExcludeForm(instance=det)
        return render(request, self.template_name, {'form':form, 'details':details, 'tours':tours})

    def post(self, request, id):
        tours = TourDetailsModel.objects.all()
        det = get_object_or_404(IncludeExcludeModel, pk=id)
        details = IncludeExcludeModel.objects.all()
        form = IncludeExcludeForm(request.POST, instance=det)
        if form.is_valid():
            form.save()
            return redirect('admin_include_exclude')
        return render(request, self.template_name, {'form':form, 'details':details, 'tours':tours})
    


class AssignIncludeExcludeView(LoginRequiredMixin, View):
    def get(self, request, tour_id):
        tour = get_object_or_404(TourDetailsModel, pk=tour_id)
        
        # Retrieve the TourIncludeExcludeModel instance for the tour
        inc_exc_instance = TourIncludeExcludeModel.objects.filter(tour=tour).first()

        # Get the selected includes and excludes from the instance if it exists
        includes = []
        excludes = []
        if inc_exc_instance:
            includes = IncludeExcludeModel.objects.filter(tourincludeexcludemodel__tour=tour, tourincludeexcludemodel__is_included=True)
            excludes = IncludeExcludeModel.objects.filter(tourincludeexcludemodel__tour=tour, tourincludeexcludemodel__is_included=False)

        # Pass the selected includes and excludes as initial data to the form
        initial_data = {'includes': includes, 'excludes': excludes}
        form = TourIncludeExcludeForm(initial=initial_data)

        return render(request, 'admin_assign_include_exclude.html', {'tour': tour, 'form': form})
    
    def post(self, request, tour_id):
        tour = TourDetailsModel.objects.get(pk=tour_id)
        form = TourIncludeExcludeForm(request.POST)
        if form.is_valid():
            includes = form.cleaned_data.get('includes', [])
            excludes = form.cleaned_data.get('excludes', [])

            # Clear existing includes/excludes for the tour
            TourIncludeExcludeModel.objects.filter(tour=tour).delete()

            # Assign new includes
            for include_item in includes:
                TourIncludeExcludeModel.objects.create(tour=tour, sentence=include_item, is_included=True)

            # Assign new excludes
            for exclude_item in excludes:
                TourIncludeExcludeModel.objects.create(tour=tour, sentence=exclude_item, is_included=False)

            return redirect('assign_include_exclude', tour_id=tour_id)  # Redirect to tour detail page or wherever you want

        return render(request, 'admin_assign_include_exclude.html', {'tour': tour, 'form': form})
    

class Faqs(LoginRequiredMixin, View):
    template_name = 'admin_faq.html'
    def get(self, request):
        tours = TourDetailsModel.objects.all()
        faqs = FaqModels.objects.all()
        form = FaqForm()
        return render(request, self.template_name, {'form':form, 'faqs':faqs, 'tours':tours})
    
    def post(self, request):
        tours = TourDetailsModel.objects.all()
        faqs = FaqModels.objects.all()
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "FAQs Added Successfully")
            return redirect('admin_faq')
        return render(request, self.template_name, {'form':form, 'faqs':faqs, 'tours':tours})
    
class EditFaqs(LoginRequiredMixin, View):
    template_name = 'admin_faq.html'

    def get(self, request, id):
        faqs = FaqModels.objects.all()
        singlefaq = get_object_or_404(FaqModels, pk=id)
        form = FaqForm(instance=singlefaq)
        return render(request, self.template_name, {'form':form, 'faqs':faqs})

    def post(self, request, id):
        faqs = FaqModels.objects.all()
        singlefaq = get_object_or_404(FaqModels, pk=id)
        form = FaqForm(request.POST, instance=singlefaq)
        if form.is_valid():
            form.save()
            return redirect('admin_faq')
        return render(request, self.template_name, {'form':form, 'faqs':faqs})
    
class DeleteFaqs(LoginRequiredMixin, View):
    def get(self, request, id):
        faqs = FaqModels.objects.get(pk=id)
        faqs.delete()
        messages.success(request, "Faqs Deleted Successfully Successfully")
        return redirect('admin_faq')  

class ToggleFaqsStatus(LoginRequiredMixin, View):
    def get(self, request, id):
        faqs = get_object_or_404(FaqModels, pk=id)
        faqs.is_global = not faqs.is_global
        faqs.save()
        messages.success(request, 'Faq Status Changes Successfully')
        return redirect('admin_faq')
  
class AssignFaqsToTourView(LoginRequiredMixin, View):
    template_name = 'admin_assign_faq.html'

    def get(self, request, tour_id):
        tour = get_object_or_404(TourDetailsModel, activity_id=tour_id)
        faqs = FaqModels.objects.all()
        assigned_faqs = TourFaqModels.objects.filter(tour_id= tour_id)
        form = AssignFaqsToTourForm()
        return render(request, self.template_name, {'tour': tour, 'faqs': faqs, 'form': form, 'assigned_faqs':assigned_faqs})

    def post(self, request, tour_id):
        tour = get_object_or_404(TourDetailsModel, activity_id=tour_id)
        faqs = FaqModels.objects.all()
        assigned_faqs = TourFaqModels.objects.filter(tour_id= tour_id)
        form = AssignFaqsToTourForm(request.POST)
        if form.is_valid():
            question_id = form.cleaned_data['question'].id
            if not TourFaqModels.objects.filter(tour_id=tour_id, question_id=question_id).exists():
                form.instance.tour_id = tour_id
                form.save()
                messages.success(request, 'FAQs assigned successfully')
                return redirect('assign_faqs_to_tour', tour_id=tour_id)  # Redirect to tour detail page or any other page
            else:
                messages.error(request, 'This FAQ is already assigned to the tour.')
        return render(request, self.template_name, {'tour': tour, 'faqs': faqs, 'form': form, 'assigned_faqs':assigned_faqs})

class UnassignFaqsToTourView(LoginRequiredMixin, View):
    def get(self, request, id):
        assigned_faq = get_object_or_404(TourFaqModels, pk=id)
        tour_id = assigned_faq.tour_id
        assigned_faq.delete()
        messages.success(request, 'FAQ unassigned successfully')
        return redirect('assign_faqs_to_tour', tour_id=tour_id)
