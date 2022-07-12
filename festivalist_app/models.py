from django.db import models
from django.contrib.auth.models import User 
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

class Festival(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    days = models.IntegerField()
    venue = models.ManyToManyField(Venue)
    date = models.DateField('festival_date')
    
    def __str__(self):
        return f"{self.name}"