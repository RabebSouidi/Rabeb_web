from django.contrib import admin
from .models import User, Doctor, Patient, Specialty
from AppointmentApp.models import Appointment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name',
                    'last_name', 'is_staff', 'is_active', 'date_joined')


class AppointmentStacked(admin.StackedInline):
    model = Appointment
    extra = 1


class DoctorPersoClass(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'license_number',
                    'phone', 'created_at', 'updated_at')

    inlines = [AppointmentStacked]


admin.site.register(Doctor, DoctorPersoClass)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'national_id',
                    'phone', 'created_at', 'updated_at')

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')