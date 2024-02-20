
from .models import CompanyProfile
from tour.models import DestinationModel, RegionModel,TourDetailsModel

def additional_context(request):
    company_profile = CompanyProfile.objects.first()
    destinations = DestinationModel.objects.all()
    activities = RegionModel.objects.filter(is_nav = True)
    all_activities = TourDetailsModel.objects.all()
    trekkings = TourDetailsModel.objects.filter(is_activity = False)
    additional_data = {'company': company_profile, 'destinations': destinations, 'activities':activities, 'all_activities':all_activities, 'trekkings':trekkings}
    return additional_data

