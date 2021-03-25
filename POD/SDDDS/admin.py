from django.contrib import admin

# Register your models here.
from .models import Category, Symptom, Disease, Doctor

admin.site.register(Category)
admin.site.register(Symptom)
admin.site.register(Disease)
admin.site.register(Doctor)

