from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #this is the route to view dragons
    path('dragons/', views.dragons_index, name='dragon_index'),
    #page for he individual dragon details
    path('dragons/<int:dragon_id>', views.dragons_detail, name='detail'),
    path('dragons/create/', views.DragonCreate.as_view(), name='dragon_create'),
    path('dragons/<int:pk>/update/', views.DragonUpdate.as_view(), name='dragon_update'),
    path('dragons/<int:pk>/delete/', views.DragonDelete.as_view(), name='dragon_delete'),
    path('cats/<int:cat_id>/add_adventurer/', views.add_adventurer, name='add_feeding'),
]


