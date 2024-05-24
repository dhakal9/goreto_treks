
from .models import CompanyProfile, MainGallaryModel, SeoModel
from tour.models import DestinationModel, RegionModel,TourDetailsModel
from random import sample
from django.template.defaultfilters import slugify

# import requests

def additional_context(request):
    company_profile = CompanyProfile.objects.first()
    seo_content = SeoModel.objects.first()
    destinations = DestinationModel.objects.all()
    gallary_images = MainGallaryModel.objects.order_by('?')[:6]
    activities = RegionModel.objects.filter(is_nav = True)
    nepal_regions = RegionModel.objects.filter(is_nav = False)
    all_activities = TourDetailsModel.objects.all()
    footer_activities = sample(list(activities), 5)
    trekkings = TourDetailsModel.objects.filter(is_activity = False)
    additional_data = {'company': company_profile, 'destinations': destinations, 'activities':activities, 'all_activities':all_activities, 'trekkings':trekkings, 'nepal_regions':nepal_regions, 'gallary_images':gallary_images, 'footer_activities':footer_activities, 'seo_content':seo_content}
    return additional_data


# def get_tripadvisor_reviews(company_name):
#     # Make request to TripAdvisor API to get reviews for ABC company
#     api_key = 'your_tripadvisor_api_key'
#     url = f'https://api.tripadvisor.com/partner/2.0/location/{company_name}/reviews?key={api_key}'
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         reviews_data = response.json()
#         # Extract number of reviews
#         num_reviews = reviews_data['review_summary']['num_reviews']
#         return num_reviews
#     else:
#         return None

# def company_reviews(request):
#     company_name = 'ABC_company'
#     num_reviews = get_tripadvisor_reviews(company_name)
#     return render(request, 'company_reviews.html', {'num_reviews': num_reviews})



