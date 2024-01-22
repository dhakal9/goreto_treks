
from django.shortcuts import render
from django.views import View
# Create your views here.

class Index(View):
    template_name = "index.html"
    def get(self,request):
        return render(request, self.template_name)
    
class Explore(View):
    template_name = "explore.html"
    def get(self, request):
        return render(request, self.template_name)