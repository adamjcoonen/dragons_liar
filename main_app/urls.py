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
    path('dragons/<int:dragon_id>/add_adventurer/', views.add_adventurer, name='add_adventurer'),
    path('dragons/<int:dragon_id>/assoc_loot/<int:loot_id>/', views.assoc_loot, name='assoc_loot'),
    path('dragons/<int:dragon_id>/assoc_loot/<int:loot_id>/', views.unassoc_loot, name='unassoc_loot'),
    path('loot/', views.LootList.as_view(), name='loot_index'),
    path('loot/<int:pk>/', views.LootDetail.as_view(), name='loot_detail'),
    path('loot/create/', views.LootCreate.as_view(), name='loot_create'),
    path('loot/<int:pk>/update/', views.LootUpdate.as_view(), name='loot_update'),
    path('loot/<int:pk>/delete/', views.LootDelete.as_view(), name='loot_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]


