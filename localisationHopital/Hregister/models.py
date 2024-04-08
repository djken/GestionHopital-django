from django.db import models
from django.contrib.auth.models import User # Import User Model model from Django

# Create your models here.
class Hopitaltracker(models.Model):
    nom = models.CharField('Nom', max_length=50)
    communaute = models.CharField('Communauté', max_length=50)
    adresse = models.CharField('Adresse', max_length=150)
    telephone = models.CharField('Telephone', max_length=20)
    site = models.URLField('Site', max_length=150, blank=True, null=True)
    courriel = models.EmailField('Courriel', max_length=150)

    class Meta:
        managed = True
        db_table = 'hopitaltracker'