from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'phone', 'email', 'experience_years')
    list_filter = ('specialization', 'experience_years')
    search_fields = ('name', 'specialization', 'email')