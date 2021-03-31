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

def sddprocessor(slist, mode): # SET_OF_ITEMS = ALLOWING_SET - PROHIBITING_SET
    
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
                allowing_symptoms=i) # getting primary keys
        )
        prohibiting_dis_set |= to_pk_set(models.Disease.objects.filter(
                prohibiting_symptoms=i)
        )
    disease_set = allowing_dis_set - prohibiting_dis_set # substracting
    for i in disease_set:
        allowing_doc_set |= to_pk_set(models.Doctor.objects.filter(
                allowing_diseases=i) # getting PK again
        )
        prohibiting_doc_set |= to_pk_set(models.Doctor.objects.filter(
                prohibiting_diseases=i)
        )
    doctor_set = allowing_doc_set - prohibiting_doc_set # substructing again
    if mode == 'external':
        for i in doctor_set:
            result.append(models.Doctor.objects.get(pk=i).doctor_name)
    elif mode == 'internal':
        result = list(doctor_set)
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
    # returns something like this:
    # {category:[symptoms], category:[symptoms],...}

#@ensure_csrf_cookie
@csrf_exempt # for testing purposes
def odapi(request):
    if request.method == 'POST': # check if the request is POST
        json_in = json.loads(request.readline()) # get the JSON
        json_out = sddprocessor(json_in['slist'], 'external') # process it
        return JsonResponse({'dlist':json_out}) # response with JSON
    return HttpResponseBadRequest('No JSON data.') # or say the user to be moron

def process_symptoms(request):
    if request.method == 'POST': # check if the request is POST
        json_out = sddprocessor(request.POST['slist'], 'internal')
        
        # TODO: add to db
        
        return HttpResponseRedirect(reverse('sddds:results', args=(json_out)))
    return HttpResponseBadRequest('Not a POST request.') 
    # or say that the user is a moron

def results(request, doctors):
    
    return render(request, 'sddds/results.html', {'doctors':doctors})
