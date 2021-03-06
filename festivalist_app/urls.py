from django.urls import path
from .import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('festivals/', views.festival_index, name='index'),
    path('festivals/saved', views.festival_saved, name='saved'),
    path('festivals/<int:festival_id>/', views.festival_detail, name='detail'),
    path('festivals/create/', views.FestivalCreate.as_view(), name = 'festival_create'),
    path('festivals/<int:pk>/update/', views.FestivalUpdate.as_view(), name='festival_update'),
    path('festivals/<int:pk>/delete/', views.FestivalDelete.as_view(), name='festival_delete'),
    path('festivals/<int:festival_id>/add_photo/', views.add_photo, name='add_photo'),
    path('venue/<int:pk>/', views.VenueDetail.as_view(), name='venue_detail'),
    path('venue/create/', views.VenueCreate.as_view(), name='venue_create'),
    path('accounts/signup/', views.signup, name='signup'),
]