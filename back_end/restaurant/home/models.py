from django.db import models

# Create your models here.

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Dessert', 'Dessert'),
    ]   
    COUNTRY_CHOICES = [
        ('Fayoum','Fayoum'),
        ('Cairo','Cairo'),
        ('Alexandria','Alexandria')
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_items/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES)

    def __str__(self):
        return self.name
    
