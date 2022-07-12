from django.urls import path
from .import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('festivals/', views.festival_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
]