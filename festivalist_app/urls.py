from django.urls import path
from .import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('festivals/', views.festival_index, name='index'),
    path('festivals/saved', views.festival_saved, name='saved'),
    path('festivals/<int:festival_id>/', views.festival_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
]