
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic import ListView, DetailView


# this is the added import for responce
from .models import Dragon, Adventurer, Loot
from .forms import AgeForm, AdventurerForm






#temp models

# class Dragon(models.Model):
#     def __init__(self, name, d_type, subtype, age,):
#         self.name = name
#         self.d_type = d_type
#         self.subtype = subtype
#         self.age = age
#         # self.lore = lore

        


# dragons = [
#     Dragon('Thermandrisinax', 'Chromatic', 'Red', 'Wyrm'),
#     Dragon('Evenlindradriel', 'Metallic', 'Silver', 'Great Wyrm'),
#     Dragon('Grunferndren', '', 'Red', 'Adult')
# ]


# Create your views here.

class DragonCreate(CreateView):
    model = Dragon
    fields = ['name', 'd_type', 'subtype', 'age', 'lore']
    success_url = '/dragons_index/'

class DragonUpdate(UpdateView):
    model = Dragon
    # if I don't place the name field it isn't called and can't rename
    fields  = ['d_type', 'subtype','age' ,'lore']

class DragonDelete(DeleteView):
    model = Dragon
    # if I don't place the name field it isn't called and can't rename
    success_url = '/dragons/'
# home view 
def home(request):
    return render(request,'home.html')
    
# this is the about function for see about dragon collector
def about(request):
    return render(request, 'about.html')

def dragons_index(request):
    dragons = Dragon.objects.all()
    return render(request, 'dragons/dragon_index.html', {'dragons' : dragons })

def dragons_detail(request, dragon_id):
    dragon = Dragon.objects.get(id=dragon_id)
    # the loot the dragon as gathered to its horde
    loot_dragon_doesnt_have = Loot.objects.exclude(id__in = dragon.loot.all().values_list('id'))
    #include the adventuerers that are 'slain'
    adventurer_form = AdventurerForm()
    return render(request, 'dragons/detail.html',
     { 'dragon': dragon, 'adventurer_form' : adventurer_form,
     # Add the toys to be displayed
    'loot': loot_dragon_doesnt_have
     })

def add_adventurer(request, dragon_id):
  # create a ModelForm instance using the data in request.POST
  form = AdventurerForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the dragon_id assigned
    new_adventurer = form.save(commit=False)
    new_adventurer.dragon_id = dragon_id
    new_adventurer.save()
  return redirect('detail', dragon_id=dragon_id)

def assoc_loot(request, cat_id, loot_id):
  # Note that you can pass a toy's id instead of the whole object
  Dragon.objects.get(id=dragon_id).loot.add(loot_id)
  return redirect('detail', dragon_id=dragon_id)