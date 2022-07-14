from django.forms import ModelForm
from .models import Festival, Venue, Photo

class FestivalForm(ModelForm):
    
    class Meta:
        model = Festival
        fields = ['name', 'days', 'venue', 'date', 'photo']
        
class VenueForm(ModelForm):
    
    class Meta:
        model = Venue
        fields = '__all__'
        
class PhotoForm(ModelForm):
    
    class Meta:
        model = Photo
        fields = '__all__'
        