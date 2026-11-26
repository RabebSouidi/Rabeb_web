
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


number_validator = RegexValidator(
    regex=r'^\d{8}$',
    message="Number must be 8 digits"
)


def validate_past_date(value):
    if value >= timezone.localdate():
        raise ValidationError(
            "La date de naissance doit être antérieure à aujourd'hui."
        )


class User(AbstractUser):
    pass


class Doctor(User):
    license_number = models.CharField(
        max_length=6,
        unique=True,
        validators=[MinLengthValidator(6)]
    )

    phone = models.CharField(
        max_length=8,
        validators=[number_validator]
    )

    specialties = models.ManyToManyField(
        'Specialty',
        related_name="doctors"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
    def __str__(self):
        return f"Dr. {self.username} - License: {self.license_number}"

class Patient(User):
    national_id = models.CharField(
        max_length=8,
        unique=True,
        validators=[number_validator]
    )

    phone = models.CharField(
        max_length=8,
        validators=[number_validator]
    )

    birth_date = models.DateField(
        validators=[validate_past_date]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
        def __str__(self):
            return f"{self.username} - National ID: {self.national_id}"


class Specialty(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Specialty"
        verbose_name_plural = "Specialties"