from sanchitha_mam import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('mytrinner/',views.about,name='about'),
    path('mam/',views.mam,name='mam'),


]
    
