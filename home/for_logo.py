
from .models import CompanyProfile
def additional_context( request):
    company_profile = CompanyProfile.objects.first()
    additional_data = {'company': company_profile }
    return additional_data