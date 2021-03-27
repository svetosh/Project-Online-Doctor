from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, QueryDict
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

import json

from . import models

def to_pk_set(qs):
    pk_set = set()
    for i in list(qs):
        pk_set.add(i.pk)
    return pk_set

def sddprocessor(slist):
    result = []
    present_symptoms = []
    allowing_dis_set = set()
    prohibiting_dis_set = set()
    allowing_doc_set = set()
    prohibiting_doc_set = set()
    for i in slist:
        present_symptoms.append(models.Symptom.objects.filter(symptom_text=i)[0].pk)
    for i in present_symptoms: # code style should be improved
        allowing_dis_set |= to_pk_set(models.Disease.objects.filter(
                allowing_symptoms=i)
        )
        prohibiting_dis_set |= to_pk_set(models.Disease.objects.filter(
                prohibiting_symptoms=i)
        )
    disease_set = allowing_dis_set - prohibiting_dis_set
    for i in disease_set:
        allowing_doc_set |= to_pk_set(models.Doctor.objects.filter(
                allowing_diseases=i)
        )
        prohibiting_doc_set |= to_pk_set(models.Doctor.objects.filter(
                prohibiting_diseases=i)
        )
    doctor_set = allowing_doc_set - prohibiting_doc_set
    for i in doctor_set:
        result.append(models.Doctor.objects.get(pk=i).doctor_name)
    return result


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

#@ensure_csrf_cookie
@csrf_exempt # for testing purposes
def odapi(request):
    if request.method == 'POST':
        json_in = json.loads(request.readline())
        json_out = sddprocessor(json_in['slist']) #dict()
        return JsonResponse({'dlist':json_out})
    return HttpResponseBadRequest('No JSON data.')
