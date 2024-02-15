# forms.py
from django import forms
from .models import CustomUser, CompanyProfile, Review, FunfactModel, OurTeamModel, BlogsModel
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm


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
        slogan1 =  forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
        slogan2 = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
        about_heading = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
        about_sub_heading = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
        about_thumbnail = forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        about_us = forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
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
    description = forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    image = forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    
    class Meta:
        model = BlogsModel
        fields = '__all__'
