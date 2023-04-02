from django.db import models
from django.contrib.auth.models import User

class Ecole(models.Model):
    nom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)

class Reservation(models.Model):
    ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
