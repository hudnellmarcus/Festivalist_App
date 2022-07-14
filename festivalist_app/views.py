from ast import Delete
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Venue, Festival, Photo
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid, boto3

S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/'
BUCKET = 'festivalist-app'

# Create your views here.
def home(request):
    return render(request, 'festivalist_app/home.html')

def festival_index(request):
        festivals = Festival.objects.all()
        return render(request, 'festivals/index.html', {'festivals': festivals})
   
    
def festival_saved(request):
        festivals = Festival.objects.filter(user=request.user)
        return render(request, 'festivals/saved.html', {'festivals': festivals})

def festival_detail(request, festival_id):
    festival = Festival.objects.get(id=festival_id)
    return render(request, 'festivals/detail.html', {
        'festival': festival })

# def assoc_venue(request, festival_id, venue_id):
#     Festival.objects.get(id=festival_id).venue.add(venue_id)
#     return redirect('detail', festival_id=festival_id)

# def assoc_venue_delete(request, festival_id, venue_id):
#     Festival.objects.get(id=festival_id).venue.remove(venue_id)
#     return redirect('detail', festival_id=festival_id)


def add_photo(request, festival_id):
    #attempt to collect the photo file data
    photo_file = request.FILES.get('photo-file', None)
    #use conditional logic to determine if file is present
    if photo_file:
    #if its present, we will create a reference to the boto3 client
        s3 = boto3.client('s3')
        #create a unique id for each photo file 
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]#this last block cuts off everything before the . in the filename
        #upload the photo file to aws s3
        try:
        #if successful
            s3.upload_fileobj(photo_file, BUCKET, key)
        #take the exchanged url and save it to the database 
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # 1) create the photo instance with photo model and provide cat_id as foreign key value
            photo = Photo(url=url, festival_id=festival_id)
            # 2) save the photo instance to the database 
            photo.save()
        #print an error message 
        except Exception as error: # this way you can print an error and type custom text
    #redirect the user to the origin page  
            print("Error uploading photo: ", error)
          
    return redirect('detail', festival_id=festival_id)

def signup(request):
    error_message = ''
    
    if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                    user = form.save()
                    login(request, user)
                    return redirect('home')
            else:
                error_message = 'Invalid sign up - try again'
    
    form = UserCreationForm()
    context = {
        'form': form,
        'error_message': error_message}
    return(render(request, 'registration/signup.html', context))

class FestivalCreate(LoginRequiredMixin, CreateView):
    model = Festival
    fields = '__all__'
    success_url = 'festivals/saved'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class FestivalUpdate(LoginRequiredMixin, UpdateView):
    model = Festival 
    
    fields = ['date', 'days']


class FestivalDelete(LoginRequiredMixin, DeleteView):
    model = Festival
    success_url = 'festivals/saved'
    
