
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

CAMPING = (
    ('Y', 'Yes'),
    ('N', 'No')
)

STATES = (
    ('AK', 'Alaska' ),
    ('AL', 'Alabama'),
    ('AR', 'Arkansas'),
    ('AZ', 'Arizona'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('IA', 'Idaho'),
    ('ID', 'Illinois'),
    ('IL', 'Indiana'),
    ('IN', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('MA', 'Massachusetts'),
    ('MD', 'Maryland'),
    ('ME', 'Maine'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MO', 'Missouri'),
    ('MS', 'Mississippi'),
    ('MT', 'Montana'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('NE', 'Nebraska'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NV', 'Nevada'),
    ('NY', 'New York'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VA', 'Virginia'),
    ('VT', 'Vermont'),
    ('WA', 'Washington'),
    ('WI', 'Wisconsin'),
    ('WV', 'West Virginia'),
    ('WY', 'Wyoming'),
)


class Venue(models.Model): 
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(
        max_length=2,
        choices=STATES)
    
    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
     return reverse('venue_detail', kwargs={'pk': self.id})

class Festival(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True)
    days = models.IntegerField()
    venue = models.ForeignKey(Venue, default=None, on_delete=models.CASCADE)
    date = models.DateField('festival_date')
    
    def __str__(self):
        return f"{self.name}"

    
    def get_absolute_url(self):
        return reverse('index', kwargs={'festival_id': self.id})
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'festival_id': self.id})

class Photo(models.Model):
    photo = models.ImageField( default="", blank=True, max_length=200)
    photo_name = models.CharField(max_length=50)
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)
    
    def __str__(self):
        return {self.festival}

    