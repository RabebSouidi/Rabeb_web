from django.db import models
from AccountApp.models import Doctor, Patient
from django.utils import timezone
from django.core.exceptions import ValidationError


class Appointment(models.Model):

    reason = models.TextField(max_length=255)

    prescription = models.FileField(
        blank=True,
        upload_to='prescriptions/'
    )

    class Status(models.TextChoices):
        PENDING = "Pending", "En attente"
        CONFIRMED = "Confirmed", "Confirmé"
        CANCELED = "Canceled", "Annulé"

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    appointment_date = models.DateTimeField()

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='appointments'
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='appointments'
    )

    def clean(self):
        super().clean()

        modified_date = self._state.adding or not (
            Appointment.objects.filter(
                pk=self.pk,
                appointment_date=self.appointment_date
            ).exists()
        )

        if modified_date and self.appointment_date:
            if self.appointment_date <= timezone.now():
                raise ValidationError(
                    "La date du rendez-vous doit être dans le futur."
                )

    def __str__(self):
        return f"Rendez-vous du {self.appointment_date} avec le Dr. {self.doctor.username} pour le patient {self.patient.username}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['doctor', 'appointment_date'],
                name='unicite_appointment_doctor_date',
                violation_error_message="Un rendez-vous existe déjà pour ce médecin à cette date."
            )
        ]

        ordering = ['appointment_date']