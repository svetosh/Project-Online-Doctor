from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest

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
    
def odapi(request):
	if request.method == 'POST':
		json_in = request.POST
		json_out = dict()
		return JsonResponse(json_out)
	return HttpResponseBadRequest('No JSON data.')
