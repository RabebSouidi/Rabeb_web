from django.db import models

# Create your models here.
class Appointment(models.Model):
    reason = models.TextField(max_length=255)
    prescription = models.FileField(blank=True,upload_to='prescriptions/')
    class Status(models.TextField):
        PENDING = "Pending","En attente"
        CONFIRMED = "Confirmed","confirmé"
        CANCELED = "Canceled","annulé"
    status = models.CharField(max_length=10, choices=Status.PENDING, default=Status.PENDING)
