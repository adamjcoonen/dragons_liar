from django.db import models
# Import the reverse function
from django.urls import reverse 
import random
# Create your models here.

# def lootRand():
#         return random.randint(1,6)
      
TYPES = (
    ('F', 'Fighter'),
    ('W', 'Wizard'),
    ('M', 'Monk'),
    ('R', 'Ranger'),
    ('B', 'Barbarian'),
    ('T', 'Thief'),
    ('C', 'Cleric'),
)

AGES = (
    ('H', 'Wyrmling'),
    ('v', 'Very Young'),
    ('y', 'Young'),
    ('J', 'Juvenile'),
    ('Y', 'Young Adult'),
    ('A', 'Adult'),
    ('O', 'Old'),
    ('V', 'Very Old'),
    ('A', 'Ancient'),
    ('W', 'Wyrm'),
    ('G', 'Great Wyrm')
)

class Dragon(models.Model):
    name = models.CharField(max_length=50)
    d_type = models.CharField(max_length=100)
    subtype = models.CharField(max_length=100)
    age = models.CharField(
        max_length=1,
        choices=AGES,
        default=[0][0],
    )
    lore = models.CharField(max_length=1000)
    # this is the many to many 
    loot = models.ManyToManyField(Loot)

    def __str__(self):
       return self.name


    def get_absolute_url(self):
       return reverse('detail', kwargs={'dragon_id' : self.id })


class Loot(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()
    magic = BooleanField()
    
    
  


# Add new Feeding model below dragon model
class Adventurer(models.Model):
    date = models.DateField('Date of incursion')
    # lootnumber = models.PositiveSmallIntegerField(default=lootRand())
    adventurer_type = models.CharField(
        max_length=1,
        #add choices
        choices=TYPES,
        #this sets the default value to be fighter or first in tuple)
        default=TYPES[0][0]
    )
    dragon = models.ForeignKey(Dragon, on_delete=models.CASCADE)
    
    def __str__(self):
        # this is a Friendly value for the TYPE of adventurer
        return f"{self.get_adventurer_type_display()} on {self.date} "
    class Meta:
        ordering = ['-date']

