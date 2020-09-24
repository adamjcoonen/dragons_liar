from django.forms import ModelForm
from .models import Dragon





class AgeForm(ModelForm):
    class Meta:
        model = Dragon
        fields = ['age']