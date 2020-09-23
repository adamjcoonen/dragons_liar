from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #this is the route to view dragons
    path('dragons/', views.dragons_index, name='dragon_index'),
    #page for he 
    path('dragons/<int:dragon_id>', views.dragons_detail, name='detail'),
    path('cats/create/', views.DragonCreate.as_view(), name='dragon_create'),
]


