from django.db import models

class Banda(models.Model):
    name = models.CharField(max_length=40)
    anio = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.anio}"
