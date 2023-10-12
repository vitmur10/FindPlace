from django.urls import path
from . import views

app_name = 'location'
urlpatterns = [
    path('', views.home, name='home'),
    # path('region/', views.region_list, name='region'),
    path('<int:region_id>/', views.region_detail, name='detail_region'),
    path('<str:name_location>/', views.location_detail, name='location'),
    path('type/<str:type_name>/', views.type_loc, name='type_loc')

]
