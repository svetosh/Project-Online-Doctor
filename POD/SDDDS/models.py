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
    allowing_symptoms = models.ManyToManyField(Symptom, blank=True, verbose_name="Возможный симптом", related_name='a_s')
    prohibiting_symptoms = models.ManyToManyField(Symptom, blank=True, verbose_name="Исключающий симптом", related_name='p_s')
    # warning_symptoms?
    def __str__(self):
        sa = ' '
        temp_list = list(self.allowing_symptoms.all())
        print (temp_list)
        for i in temp_list:
            sa+= i.symptom_text + '; '
        sp = ' '
        temp_list = list(self.prohibiting_symptoms.all())
        print (temp_list)
        for i in temp_list:
            sp+= i.symptom_text + '; '
        return self.disease_name + '  [' + sa[:-2] + '][' + sp[:-2] + ']'

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100, unique=True, verbose_name="Специалист")
    allowing_diseases = models.ManyToManyField(Disease, blank=True, verbose_name="Лечит", related_name='a_d')
    prohibiting_diseases = models.ManyToManyField(Disease, blank=True, verbose_name="Не лечит", related_name='p_d')
    
    def __str__(self):
        sa = ' '
        temp_list = list(self.allowing_diseases.all())
        for i in temp_list:
            sa+= i.disease_name + '; '
        sp = ' '
        temp_list = list(self.prohibiting_diseases.all())
        for i in temp_list:
            sp+= i.disease_name + '; '
        return self.doctor_name + '  [' + sa[:-2] + '][' + sp[:-2] + ']'

