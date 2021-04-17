from django.db import models
from django.conf import settings

# Everything presented here should be improved,
# i.e. the implementation in prolog had an ability to make such constructions 
# like "(SYMPTOM_0 and SYMPTOM_1) or (SYMPTOM_2 and SYMPTOM_3 and not SYMPTOM4)"
# but now we are limited to two sets of symptoms. The same is applicable to the
# Disease model and its relation with Doctor class.

# Constants
B = '  ['  # begin
M = ']  [' # middle
E = ' ]'      # end
SEPARATOR = '; '

class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name="Категория симптомов")
    
    def __str__(self):
        return self.category_name

class Symptom(models.Model):
    symptom_text = models.CharField(max_length=500, unique=True, verbose_name="Симптом")
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, verbose_name="Категория")
    
    def __str__(self):
        return self.symptom_text

class Disease(models.Model):
    disease_name = models.CharField(max_length=200, unique=True, verbose_name="Название класса заболеваний")
    allowing_symptoms = models.ManyToManyField(Symptom, blank=True, verbose_name="Возможные симптомы", related_name='a_s')
    prohibiting_symptoms = models.ManyToManyField(Symptom, blank=True, verbose_name="Исключающие симптомы", related_name='p_s')
    
    def __str__(self):
        sa = ' '
        temp_list = list(self.allowing_symptoms.all())
        for i in temp_list:
            sa+= i.symptom_text + SEPARATOR
        sp = ' '
        temp_list = list(self.prohibiting_symptoms.all())
        for i in temp_list:
            sp+= i.symptom_text + SEPARATOR
        return self.disease_name + B + sa[:-2] + M + sp[:-2] + E

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100, unique=True, verbose_name="Специалист")
    allowing_diseases = models.ManyToManyField(Disease, blank=True, verbose_name="Лечит", related_name='a_d')
    # ~ prohibiting_diseases = models.ManyToManyField(Disease, blank=True, verbose_name="Не лечит", related_name='p_d')
    
    def __str__(self):
        sa = ' '
        temp_list = list(self.allowing_diseases.all())
        for i in temp_list:
            sa+= i.disease_name + SEPARATOR
        # ~ sp = ' '
        # ~ temp_list = list(self.prohibiting_diseases.all())
        # ~ for i in temp_list:
            # ~ sp+= i.disease_name + SEPARATOR
        return self.doctor_name + B + sa[:-2] + E #M + sp[:-2] + 



class HistoryEntry(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
	symptoms = models.CharField(max_length=1000, verbose_name="Введённые симптомы") 
	result = models.CharField(max_length=1000, verbose_name="Рекомендованные специалисты")
