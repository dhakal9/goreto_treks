# forms.py
from django import forms
from .models import CustomUser, CompanyProfile, Review, FunfactModel, OurTeamModel, BlogsModel, CsrModel, MainGallaryModel, WhyUsModel, SeoModel
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django_summernote.widgets import SummernoteWidget

class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=50, required=True, widget=forms.EmailInput(attrs={'placeholder':'abc@email.com', 'class':'form-control'}))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'}))


# class HomePageForm(CompanyProfile):
#     first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder':'First Name', 'class':'form-control'}))
#     last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder':'Last Name', 'class':'form-control'}))
#     email = forms.EmailField( max_length=50, required=True, widget=forms.EmailInput(attrs={'placeholder':'abc@email.com', 'class':'form-control'}))
#     phone = PhoneNumberField(required=True, widget=forms.TextInput(attrs={'placeholder': '9876543210','class': 'form-control'}))
#     password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'}))
#     password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'}))
    
#     class Meta:
#         model = CustomUser
#         fields= ['first_name', 'last_name', 'email', 'phone', 'password1', 'password2']

class CompanyProfileForm(forms.ModelForm):
        name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder':'xyz treks', 'class':'form-control'}))
        email = forms.EmailField(max_length=50, required=True, widget=forms.EmailInput(attrs={'placeholder':'abc@email.com', 'class':'form-control'}))
        address = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
        contact = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
        telephone = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
        slogan1 =  forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
        slogan2 = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
        about_heading = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
        about_sub_heading = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
        about_thumbnail = forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        about_us = forms.CharField(widget=SummernoteWidget(attrs={'class': 'form-control', 'summernote': {'height': '500px', 'width': '100%'}}))
        why_us = forms.CharField(widget=SummernoteWidget(attrs={'class': 'form-control', 'summernote': {'height': '500px', 'width': '100%'}}))
        home_image = forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        banner1_image = forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        banner2_image = forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        logo_image = forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        video_thumbnail_image = forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        video_link = forms.URLInput(attrs={'class':'form-control'})
    
        class Meta:
            model = CompanyProfile
            fields = '__all__'

    
    
class ReviewForm(forms.ModelForm):

    team_image = forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
    name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    position = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
    is_active = forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    
    class Meta:
        model = Review
        fields = '__all__'

class FunfactForm(forms.ModelForm):
    travellers = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    places = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    miles = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    years = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = FunfactModel
        fields = '__all__'

class OurTeamForm(forms.ModelForm):
    name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(widget=SummernoteWidget(attrs={'class': 'form-control', 'summernote': {'height': '500px', 'width': '100%'}}))
    # message = forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    position = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    team_image = forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    facebook_link = forms.URLInput(attrs={'class':'form-control'})
    instagram_link = forms.URLInput(attrs={'class':'form-control'})
    
    class Meta:
        model = OurTeamModel
        fields = '__all__'

class ContactUs(forms.Form):
    username = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    
class BlogsForm(forms.ModelForm):
    title = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=SummernoteWidget(attrs={'class': 'form-control', 'summernote': {'height': '500px', 'width': '100%'}}))
    image = forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    
    class Meta:
        model = BlogsModel
        fields = '__all__'

class CsrForm(forms.ModelForm):
    title = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=SummernoteWidget(attrs={'class': 'form-control', 'summernote': {'height': '500px', 'width': '100%'}}))
    image = forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    
    class Meta:
        model = CsrModel
        fields = '__all__'
    
class MainGallaryForm(forms.ModelForm):
    image = forms.ImageField(required=True, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    
    class Meta:
        model = MainGallaryModel
        fields = '__all__'

class WhyUsForms(forms.ModelForm):
    title = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=SummernoteWidget(attrs={'class': 'form-control', 'summernote': {'height': '500px', 'width': '100%'}}))
    
    class Meta:
        model = WhyUsModel
        fields = '__all__'

class PlanningTripForm(forms.Form):
    firstname = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'type':'text'}))
    lastname = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'type':'text'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'type':'email', 'placeholder':'Your Email', 'name':'email'}))
    tour_name= forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'type':'text'}))
    address1 = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'type':'text'}))
    address2 = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'type':'text'}))
    city = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'type':'text'}))
    zip_code = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'type':'text' }))
    state = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'type':'text'}))
    country = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'type':'text'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2, "placeholder":"Message"}))


class SeoForm(forms.ModelForm):
    discription = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))

    class Meta:
        model = SeoModel
        fields = '__all__'