from django.db import models


class Probleme(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Solution(models.Model):
    probleme = models.ForeignKey(Probleme, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description