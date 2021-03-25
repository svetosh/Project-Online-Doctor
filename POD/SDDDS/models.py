from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name="Категория симптомов")
    def __str__(self):
        return self.category_name

class Symptom(models.Model):
    symptom_text = models.CharField(max_length=500, unique=True, verbose_name="Симптом")
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, verbose_name="Категория")
    
    def __str__(self):
        return str(self.category)+': '+self.symptom_text

class Disease(models.Model):
    disease_name = models.CharField(max_length=200, unique=True, verbose_name="Название класса")
    #allowing_
    symptoms = models.ManyToManyField(Symptom, verbose_name="Возможный симптом")
    #prohibiting_symtoms = models.ManyToManyField(Symptom, verbose_name="Исключающий симптом")
    # warning_symptoms?
    def __str__(self):
        s = ': '
        for i in list(self.symptoms.all()):
            s+= i.symptom_text + '; '
        return self.disease_name + s[:-2]

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100, unique=True, verbose_name="Специалист")
    #allowing_
    diseases = models.ManyToManyField(Disease, verbose_name="Лечит")
    #prohibiting_diseases = models.ManyToManyField(Disease, verbose_name="Не лечит")
    def __str__(self):
        s = ': '
        for i in list(self.diseases.all()):
            s+= i.disease_name + '; '
        return self.doctor_name + s[:-2]

