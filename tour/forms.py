from django import forms
from .models import DestinationModel, RegionModel, TourDetailsModel, ItinatyModel, GallaryModel, IncludeExcludeModel


class DestinationForm(forms.ModelForm):
    name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Country Name', 'class': 'form-control'}))
    slogan = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Where culture meets nature', 'class': 'form-control'}))
    description = forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'my-checkbox-class'}))
    image = forms.ClearableFileInput(attrs={'class': 'form-control-file'})

    class Meta:
        model = DestinationModel
        fields = '__all__'



class RegionForm(forms.ModelForm):
    
    name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    image = forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    destination = forms.ModelChoiceField(queryset=DestinationModel.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

      


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['destination'].queryset = DestinationModel.objects.all()
        self.fields['destination'].label_from_instance = self.get_destination_name

    def get_destination_name(self, instance):
        return instance.name   
    
    class Meta:
        model = RegionModel
        fields = "__all__"

class TourDetailsForm(forms.ModelForm):
    destination = forms.ModelChoiceField(queryset=DestinationModel.objects.all(), 
                                         widget=forms.Select(attrs={'class': 'form-control'}))
    region = forms.ModelChoiceField(queryset=RegionModel.objects.all(), 
                                     widget=forms.Select(attrs={'class': 'form-control'}))
    
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    depature = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))
    start_end = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    max_price = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    transport = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    season = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    altitude = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    days = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    map = forms.URLField(max_length=2048, required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    map_overview = forms.CharField(widget=forms.Textarea(attrs={'id': 'editor'}))
    image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    is_activity = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'my-checkbox-class'}))
    is_acttraction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'my-checkbox-class'}))
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'my-checkbox-class'}))
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['region'].queryset = RegionModel.objects.all()
        self.fields['region'].label_from_instance = self.get_region_name
        self.fields['destination'].queryset = DestinationModel.objects.all()
        self.fields['destination'].label_from_instance = self.get_destination_name

    def get_destination_name(self, instance):
        return instance.name   
    
    def get_region_name(self, instance):
        return instance.name

    class Meta:
        model = TourDetailsModel
        fields = "__all__"
        


class ItinaryForm(forms.ModelForm):
    tour = forms.ModelChoiceField(queryset=TourDetailsModel.objects.all(), 
                                     widget=forms.Select(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    day = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    start_end = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.Textarea(attrs={'class': 'form-control', 'rows': 5})

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tour'].queryset = TourDetailsModel.objects.all()
        self.fields['tour'].label_from_instance = self.get_tour_name
    
    def get_tour_name(self, instance):
        return instance.name   
        
    class Meta:
        model = ItinatyModel
        fields ="__all__"
        
class GallaryForm(forms.ModelForm):
    tour = forms.ModelChoiceField(queryset=TourDetailsModel.objects.all(), 
                                     widget=forms.Select(attrs={'class': 'form-control'}))
    image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tour'].queryset = TourDetailsModel.objects.all()
        self.fields['tour'].label_from_instance = self.get_tour_name
    
    def get_tour_name(self, instance):
        return instance.name  
    
    class Meta:
        model = GallaryModel
        fields ="__all__"


class BookingForm(forms.Form):
    username = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'type':'text', 'placeholder':'Your Name'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'type':'email', 'placeholder':'Your Email', 'name':'email'}))
    phone = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'type':'text', 'name':'phone', 'placeholder':'Phone'}))
    date = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder':'dd/mm/yyyy', 'id':'datepicker'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2, "placeholder":"Message"}))


class InqueryForm(forms.Form):
    username = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={ 'type':'text', 'placeholder':'Your Name', 'id':'name'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={ 'type':'email', 'placeholder':'Your Email', 'name':'email', 'id':'email'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Message',}))

class IncludeExcludeForm(forms.ModelForm):
    name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
     
    class Meta:
        model = IncludeExcludeModel
        fields ="__all__"
    