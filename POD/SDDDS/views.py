from django.shortcuts import render

from django.http import HttpResponse, JsonResponse


def index(request):
    return JsonResponse({"Hello, world.":"You're at the Symptom-Disease-Doctor Data Service index."})
