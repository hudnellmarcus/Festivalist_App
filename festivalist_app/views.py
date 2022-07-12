from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Venue, Festival
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    return render(request, 'festivalist_app/home.html')

def festival_index(request):
    user = request.user
    
    if user: 
        festivals = Festival.objects.filter(user=request.user)
        return render(request, 'festivals/index.html', {'festivals': festivals})

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