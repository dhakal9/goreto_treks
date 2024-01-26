from django import forms
from .models import DestinationModel

class DestinationForm(forms.ModelForm):
    name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Country Name', 'class': 'form-control'}))
    slogan = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Where culture meets nature', 'class': 'form-control'}))
    description = forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'my-checkbox-class'}))
    image = forms.ClearableFileInput(attrs={'class': 'form-control-file'})

    class Meta:
        model = DestinationModel
        fields = '__all__'

