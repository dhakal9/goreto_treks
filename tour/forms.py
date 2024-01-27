from django import forms
from .models import DestinationModel, RegionModel

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