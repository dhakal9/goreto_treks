
from .models import CompanyProfile
from tour.models import DestinationModel, RegionModel

def additional_context( request):
    company_profile = CompanyProfile.objects.first()
    destinations = DestinationModel.objects.all()
    activities = RegionModel.objects.filter(is_nav = True)
    additional_data = {'company': company_profile, 'destinations': destinations, 'activities':activities }
    return additional_data

