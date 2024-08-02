from django import forms
from .models import DestinationModel, RegionModel, TourDetailsModel, ItinatyModel, GallaryModel, IncludeExcludeModel, FaqModels, TourFaqModels, SpecialModels
from django_summernote.widgets import SummernoteWidget
from django.forms import inlineformset_factory
# from tinymce.widgets import TinyMCE
from ckeditor.widgets import CKEditorWidget

class DestinationForm(forms.ModelForm):
    name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Country Name', 'class': 'form-control'}))
    slogan = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Where culture meets nature', 'class': 'form-control'}))
    description = forms.CharField(widget=CKEditorWidget(attrs={'class': 'ckeditor', 'id':'editor1'}))
    image = forms.ImageField(required=True, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = DestinationModel
        fields = '__all__'


class RegionForm(forms.ModelForm):
    name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=CKEditorWidget(attrs={'class': 'ckeditor', 'id':'editor1'}))
    image = forms.ImageField(required=True, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
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
    description = forms.CharField(widget=CKEditorWidget(attrs={'class': 'ckeditor', 'id':'editor1'}))
    depature = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    start_end = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    max_price = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    transport = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    season = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    altitude = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    days = forms.CharField(max_length=500, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    map = forms.URLField(max_length=2048, required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    map_overview = forms.CharField(widget=CKEditorWidget(attrs={'class': 'ckeditor', 'id':'editor'}))
    image = forms.ImageField(required=True, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    is_activity = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'my-checkbox-class'}))
    is_attraction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'my-checkbox-class'}))
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'my-checkbox-class'}))
    difficulty_level = forms.ChoiceField(choices=TourDetailsModel.DIFFICULTY_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    itinary_pdf = forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    total_reviews = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    star_rating = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price_1 = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price_2 = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price_35 = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price_510 = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
     
       
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
    name = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    day = forms.CharField(max_length=6, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # start_end = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=SummernoteWidget(attrs={'class': 'form-control', 'summernote': {'height': '300px', 'width': '100%'}}))

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tour'].queryset = TourDetailsModel.objects.all()
        self.fields['tour'].label_from_instance = self.get_tour_name
    
    def get_tour_name(self, instance):
        return instance.name   

        
    class Meta:
        model = ItinatyModel
        fields ="__all__"

ItineraryFormSet = inlineformset_factory(TourDetailsModel, ItinatyModel, form=ItinaryForm, extra=1)

# from django import forms
# from .models import TourDetailsModel, ItinatyModel
# from django_summernote.widgets import SummernoteWidget

# class ItinaryForm(forms.ModelForm):
#     tour = forms.ModelChoiceField(queryset=TourDetailsModel.objects.all(), 
#                                      widget=forms.Select(attrs={'class': 'form-control'}))
#     number_of_days = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))
#     description = forms.CharField(widget=SummernoteWidget(attrs={'class': 'form-control', 'summernote': {'height': '300px', 'width': '100%'}}))

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['tour'].queryset = TourDetailsModel.objects.all()
#         self.fields['tour'].label_from_instance = self.get_tour_name

#     def get_tour_name(self, instance):
#         return instance.name   

#     class Meta:
#         model = ItinatyModel
#         fields = ['tour', 'number_of_days', 'description']



        
class GallaryForm(forms.ModelForm):
    tour = forms.ModelChoiceField(queryset=TourDetailsModel.objects.all(), 
                                     widget=forms.Select(attrs={'class': 'form-control'}))
    image = forms.ImageField(required=True, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    
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


class TourIncludeExcludeForm(forms.ModelForm):
    class Meta:
        model = TourDetailsModel
        fields = ['includes', 'excludes']

    includes = forms.ModelMultipleChoiceField(
        queryset=IncludeExcludeModel.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    excludes = forms.ModelMultipleChoiceField(
        queryset=IncludeExcludeModel.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the label field for each choice
        self.fields['includes'].label_from_instance = lambda obj: obj.name
        self.fields['excludes'].label_from_instance = lambda obj: obj.name

        # Pre-select the items based on the instance being edited
        if self.instance.pk:
            self.fields['includes'].initial = self.instance.includes.all()
            self.fields['excludes'].initial = self.instance.excludes.all()

class FaqForm(forms.ModelForm):
    question = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    answer = forms.CharField(widget=CKEditorWidget(attrs={'class': 'ckeditor', 'id':'editor1'}))
    class Meta:
        model = FaqModels
        fields ="__all__"
        
    def __str__(self):
        return self.question
    
class AssignFaqsToTourForm(forms.ModelForm):
    class Meta:
        model = TourFaqModels
        fields = ['question']

    def label_from_instance(self, obj):
        return obj.question

class SpecialForm(forms.ModelForm):
    trekking_des = forms.CharField(widget=CKEditorWidget(attrs={'class': 'ckeditor', 'id':'editor1'}))
    goreto_special_des = forms.CharField(widget=CKEditorWidget(attrs={'class': 'ckeditor'}))
    class Meta:
        model = SpecialModels
        fields ="__all__"
        