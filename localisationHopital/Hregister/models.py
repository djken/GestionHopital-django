from django.db import models

# Create your models here.
class Hopitaltracker(models.Model):
    nom = models.CharField('Nom', max_length=50) # text or string
    communaute = models.CharField('Communauté', max_length=50)
    adresse = models.CharField('Adresse', max_length=150)
    telephone = models.CharField('Telephone', max_length=20) 
    site = models.URLField('Site', max_length=150, blank=True, null=True) # http:
    courriel = models.EmailField('Courriel', max_length=150)

    class Meta:
        managed = True
        db_table = 'hopitaltracker' 

# python manage.py makemigrations
# python migrate