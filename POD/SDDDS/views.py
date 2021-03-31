from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseRedirect 
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.urls import reverse

import json

from . import models

def to_pk_set(qs):
    pk_set = set()
    for i in list(qs):
        pk_set.add(i.pk)
    return pk_set

def sddprocessor(slist, mode): # SET_OF_ITEMS = ALLOWING_SET - PROHIBITING_SET
    
    dlist = []
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
    for i in doctor_set:
        dlist.append(models.Doctor.objects.get(pk=i).doctor_name)
    if mode == 'external':
        result = {'dlist' : dlist}
    elif mode == 'internal':
        result = {'dlist' : dlist, 'pk_list' : list(doctor_set)}
    return result

def get_symptoms():
    response = dict()
    cat_list = list(models.Category.objects.all())
    symp_names = []
    for i in cat_list:
        symp_list = list(i.symptom_set.all())
        for j in symp_list:
            symp_names.append(j.symptom_text)
        response[i.category_name] = symp_names[:]
        symp_names.clear()
    return response



def index_json(request):
    jresponse = get_symptoms()
    return JsonResponse(jresponse)
    # returns something like this:
    # {category:[symptoms], category:[symptoms],...}

#@ensure_csrf_cookie
@csrf_exempt # for testing purposes
def odapi(request):
    if request.method == 'POST': # check if the request is POST
        json_in = json.loads(request.readline()) # get the JSON
        json_out = sddprocessor(json_in['slist'], 'external') # process it
        return JsonResponse(json_out) # response with JSON
    return HttpResponseBadRequest('No JSON data.') # or say the user to be moron



def index(request):
    symptoms = models.Category.objects.all()
    return render(request, 'SDDDS/index.html', {'symptoms':symptoms})

def process_symptoms(request):
    if request.method == 'POST': # check if the request is POST
        json_out = {'test':'api'}#sddprocessor(request.POST['slist'], 'internal')
        print(request.POST.dict())
        # TODO: add to db
        
        return HttpResponseRedirect(reverse('sddds:results', args=(json_out)))
    return HttpResponseBadRequest('Not a POST request.') 
    # say the user is too curious

def results(request, doctors):
    return render(request, 'SDDDS/results.html', {'doctors':doctors})
