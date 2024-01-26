
from .models import CompanyProfile
from tour.models import DestinationModel

def additional_context( request):
    company_profile = CompanyProfile.objects.first()
    destinations = DestinationModel.objects.all()
    additional_data = {'company': company_profile, 'destinations': destinations }
    return additional_data

