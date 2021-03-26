from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from . import models

def index(request):
    jresponse = dict()
    cat_list = list(models.Category.objects.all())
    symp_names = []
    for i in cat_list:
        symp_list = list(i.symptom_set.all())
        for j in symp_list:
            symp_names.append(j.symptom_text)
        jresponse[i.category_name] = symp_names[:]
        symp_names.clear()
    return JsonResponse(jresponse)
