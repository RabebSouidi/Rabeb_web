from django.contrib import admin
from AppointmentApp.models import Appointment

@admin.action(description='Confirmer les rendez-vous sélectionnés')
def confirm_appointment(modeladmin, request, queryset):
    queryset.update(status='CONFIRMED')



@admin.register(Appointment)
class AppointmentAdminPers(admin.ModelAdmin):
    actions = [confirm_appointment]
    
    list_display = ('reason', 'status', 'appointment_date', 'doctor', 'patient')

    list_filter = ('status', 'appointment_date')

    list_editable = ('status',)

    search_fields = ('reason', 'status')

    ordering = ('-appointment_date',)

    fieldsets = (
        ('Description', {
            'fields': ('reason', 'prescription', 'status')
        }),
        ('Details', {
            'fields': ('appointment_date', 'doctor', 'patient')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    readonly_fields = ('created_at', 'updated_at')