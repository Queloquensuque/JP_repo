
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=40)
    capital = models.CharField(max_length=40)
    #description = models.TextField()
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.capital}"


