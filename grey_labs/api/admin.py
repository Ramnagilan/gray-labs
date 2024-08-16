from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Department, Doctor, PatientRecordNew, DoctorPatientRelationship


from django.contrib import admin
from .models import Department, Doctor, PatientRecordNew, DoctorPatientRelationship

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'location')  # Fields to display in the table
    search_fields = ('name', 'specialization')  # Fields to search by
    list_filter = ('specialization',)  # Filters on the side

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'department')  # Fields to display
    search_fields = ('user__username', 'department__name')  # Fields to search by
    list_filter = ('department',)  # Filters on the side

@admin.register(PatientRecordNew)
class PatientRecordNewAdmin(admin.ModelAdmin):
    list_display = ('record_id', 'patient', 'doctor', 'created_date')  # Fields to display
    search_fields = ('patient__username', 'doctor__user__username')  # Fields to search by
    list_filter = ('created_date', 'doctor__department')  # Filters on the side

@admin.register(DoctorPatientRelationship)
class DoctorPatientRelationshipAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient')  # Fields to display
    search_fields = ('doctor__user__username', 'patient__username')  # Fields to search by
