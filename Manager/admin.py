from django.contrib import admin
from Manager.models import Department, Doctor, OperatingRoom, Surgery, Patient

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "department"]
    search_fields = ["username", "first_name", "last_name", "department__name"]

@admin.register(OperatingRoom)
class OperatingRoomAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

@admin.register(Surgery)
class SurgeryAdmin(admin.ModelAdmin):
    list_display = ["surgery_name", "start_time", "operating_room"]
    search_fields = ["surgery_name", "operating_room__name"]

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "doctor", "department", "room_number", "operation"]
    search_fields = ["first_name", "last_name", "doctor__username", "department__name", "operation__surgery_name"]
