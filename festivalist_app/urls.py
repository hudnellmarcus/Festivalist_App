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
    path('accounts/signup/', views.signup, name='signup'),
]