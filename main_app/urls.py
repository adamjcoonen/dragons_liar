from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #this is the route to view dragons
    path('dragons/', views.dragon_index, name='index'),
]


