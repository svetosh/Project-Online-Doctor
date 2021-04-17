from django.contrib import admin

from .models import Category, Symptom, Disease, Doctor


class SymptomAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,               {'fields': ['symptom_text','category']}),
    ]
    list_display = ('symptom_text','category')
    list_filter = ['category']
    search_fields = ['symptom_text']

class DiseaseAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,               {'fields': ['disease_name']}),
    ('Симптомы',         {'fields': ['allowing_symptoms','prohibiting_symptoms']})
    ]
    search_fields = ['disease_name']
    list_display = ['disease_name']
    
    
class DoctorAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,               {'fields': ['doctor_name']}),
    ('Классы заболеваний',         {'fields': ['allowing_diseases']})
    ]
    search_fields = ['doctor_name']

admin.site.register(Category)
admin.site.register(Symptom, SymptomAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(Doctor, DoctorAdmin)
