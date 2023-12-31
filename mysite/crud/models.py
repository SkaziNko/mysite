from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre =  models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email}"

