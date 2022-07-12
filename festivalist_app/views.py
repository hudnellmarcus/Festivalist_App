from ast import Delete
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Venue, Festival
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




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

def assoc_venue(request, festival_id, venue_id):
    Festival.objects.get(id=festival_id).venue.add(venue_id)
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