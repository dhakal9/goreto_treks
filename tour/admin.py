from django.contrib import admin
from tour.models import DestinationModel, RegionModel, ItinatyModel, TourDetailsModel
# Register your models here.

admin.site.register(DestinationModel)
admin.site.register(RegionModel)
admin.site.register(ItinatyModel)
admin.site.register(TourDetailsModel)