
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=40)
    capital = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name} - {self.capital}"