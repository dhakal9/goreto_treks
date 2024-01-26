from django.shortcuts import render, redirect
from django.views import View
from .models import DestinationModel
from .forms import DestinationForm

class Destination(View):
    template_name = "admin_destination.html"
    form_class = DestinationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_destination')  # Replace 'your_redirect_url' with the actual URL to redirect after form submission

        return render(request, self.template_name, {'form': form})
