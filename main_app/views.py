
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# this is the added import for responce
from .models import Dragon, Adventurer, Loot
from .forms import  AdventurerForm






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

class DragonCreate(LoginRequiredMixin, CreateView):
    model = Dragon
    fields = ['name', 'd_type', 'subtype', 'age', 'lore']
    success_url = '/dragons_index/'

    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
        return super().form_valid(form)

class DragonUpdate(LoginRequiredMixin, UpdateView):
    model = Dragon
    # if I don't place the name field it isn't called and can't rename
    fields  = ['d_type', 'subtype','age' ,'lore']

class DragonDelete(LoginRequiredMixin, DeleteView):
    model = Dragon
    # if I don't place the name field it isn't called and can't rename
    success_url = '/dragons/'
# home view 
def home(request):
    return render(request,'home.html')
    
# this is the about function for see about dragon collector
def about(request):
    return render(request, 'about.html')
@login_required
def dragons_index(request):
    dragons = Dragon.objects.all()
    return render(request, 'dragons/dragon_index.html', {'dragons' : dragons })
@login_required
def dragons_detail(request, dragon_id):
    dragon = Dragon.objects.get(id=dragon_id)
    # the loot the dragon as gathered to its horde
    loot_dragon_doesnt_have = Loot.objects.exclude(id__in = dragon.loot.all().values_list('id'))
    #include the adventuerers that are 'slain'
    adventurer_form = AdventurerForm()
    return render(request, 'dragons/detail.html',
     { 'dragon': dragon, 'adventurer_form' : adventurer_form,
     # Add the loot to be displayed
    'loot': loot_dragon_doesnt_have})
@login_required
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
@login_required
def assoc_loot(request, dragon_id, loot_id):
  # Note that you can pass a loot's id instead of the whole object
    Dragon.objects.get(id=dragon_id).loot.add(loot_id)
    return redirect('detail', dragon_id=dragon_id)
@login_required
def unassoc_loot(request, dragon_id, loot_id):
  # Note that you can pass a loot's id instead of the whole object
    Dragon.objects.get(id=dragon_id).loot.remove(loot_id)
    return redirect('detail', dragon_id=dragon_id)

class LootList(LoginRequiredMixin, ListView):
    model = Loot
    

class LootDetail(LoginRequiredMixin, DetailView):
    model = Loot

class LootCreate(LoginRequiredMixin, CreateView):
    model = Loot
    fields = '__all__'
    success_url = '/loot/'

class LootUpdate(LoginRequiredMixin, UpdateView):
    model = Loot
    fields = ['name', 'value']

class LootDelete(LoginRequiredMixin, DeleteView):
    model = Loot
    success_url = '/loot/'



def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      # This is how we log in a user via code
      login(request, user)
      return redirect('dragon_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)