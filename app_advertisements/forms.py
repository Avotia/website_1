from django.forms import ModelForm, TextInput, Textarea, NumberInput, CheckboxInput, FileInput
from .models import Advertisement

class AdvertisementForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control from-control-lg'}),
            'description': Textarea(attrs={'class': 'form-control from-control-lg'}),
            'price': NumberInput(attrs={'class': 'form-control from-control-lg'}),
            'auction': CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': FileInput(attrs={'class': 'form-control from-control-lg'}),
        }

form = AdvertisementForm()