from django.db import models
# import the reverse 
from django.urls import reverse 

# Create your models here.



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

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('detail', kwargs={'dragon_id' : self.id })
