from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Wishlist(models.Model):
    nom = models.CharField(max_length=64)
    description = models.TextField(max_length=1000)
    prix = models.FloatField()
    note = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])