from django.forms import ModelForm
from .models import Dragon, Adventurer





# class AgeForm(ModelForm):
#     class Meta:
#         model = Dragon
#         fields = ['age']



class AdventurerForm(ModelForm):
  class Meta:
    model = Adventurer
    fields = ['date', 'adventurer_type']