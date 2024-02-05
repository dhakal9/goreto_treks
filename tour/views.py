from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import DestinationModel, RegionModel, TourDetailsModel, ItinatyModel
from .forms import DestinationForm, RegionForm, TourDetailsForm, ItinatyForm

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
    
# class CloseTicket(View):
#     def get(self, request, ticket_id):
#         user_project_id = ProjectUser.objects.filter(user_id=request.user.id).values_list('project_id', flat=True)
#         open_ticket = Tickets.objects.get(prj_id__in=user_project_id, ticket_id=ticket_id)
#         open_ticket.closed_status = True
#         open_ticket.save()
#         messages.success(request, 'Ticket Closed Successfullly')
#         return redirect('my_tickets')
    
class Tourlist(View):
    template_name = 'tourlist.html'
    def get(self, request, pk):
        region = RegionModel.objects.get(pk=pk)
        tours = TourDetailsModel.objects.all()
        return render(request, self.template_name, {'region':region, 'tours':tours})
        
class AdminTour(View):
    template_name = 'admin_tour.html'

    def get(self, request):
        form = TourDetailsForm()
        form1 = ItinatyForm()
        tours = TourDetailsModel.objects.all()
        return render(request, self.template_name, {'form': form, 'form1':form1, 'tours':tours})

    def post(self, request):
        tours = TourDetailsModel.objects.all()
        form1 = ItinatyForm()
        form = TourDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_tour')  # Replace 'your_redirect_url' with the actual URL to redirect after form submission

        return render(request, self.template_name, {'form': form, 'form1':form1, 'tours':tours})

class TourDeatails(View):
    template_name = 'tour_details.html'
    def get(self, request, pk):
        tour_details = TourDetailsModel.objects.get(pk=pk)
        return render(request, self.template_name, {'tour_details':tour_details})

