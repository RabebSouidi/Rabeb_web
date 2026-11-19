from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):

    pass
class Doctor(User):
    license_number = models.CharField(max_length=6, unique=True)
    phone=models.CharField(max_length=8)

class Patient(User):
    national_id = models.CharField(max_length=9, unique=True)
    birth_date = models.DateField()

class specialty(models.Model):
    name = models.CharField(max_length=255)
