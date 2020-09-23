

from django.shortcuts import render
from django.views.generic.edit import CreateView

# this is the added import for responce
from .models import Dragon






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
    return render(request, 'dragons/detail.html', { 'dragon': dragon})


class DragonCreate(CreateView):
    model = Dragon
    fields = ['name', 'd_type', 'subtype', 'age' , 'lore' ]


