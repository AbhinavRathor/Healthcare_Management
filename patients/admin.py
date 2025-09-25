from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'phone', 'email', 'created_by')
    list_filter = ('gender', 'created_at')
    search_fields = ('name', 'email', 'phone')