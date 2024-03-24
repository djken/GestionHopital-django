from django.db import models

# Create your models here.
class TblHospitaltracker(models.Model):
    name = models.CharField(max_length=255)
    community = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    web_address = models.CharField(max_length=255, blank=True, null=True)
    email_address = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tbl_hospitaltracker'