from django.db import models

# Create your models here.


class Dragon:
    def __init__(self, name, d_type, subtype, age,):
        self.name = name
        self.type = d_type
        self.subtype = subtype
        self.age = age
        # self.lore = lore

        


dragons = [
    Dragon('Thermandrisinax', 'Chromatic', 'Red', 'Wyrm'),
    Dragon('Evenlindradriel', 'Metallic', 'Silver', 'Great Wyrm'),
    Dragon('Grunferndren', '', 'Red', 'Adult')
]