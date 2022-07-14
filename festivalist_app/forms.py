from django.forms import ModelForm
from .models import Festival, Venue

class FestivalForm(ModelForm):
    
    class Meta:
        model = Festival
        fields = ['name', 'days', 'venue', 'date', 'photo']
        
class VenueForm(ModelForm):
    
    class Meta:
        model = Venue
        fields = '__all__'