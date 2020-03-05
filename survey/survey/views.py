import json
from django.core import serializers
from django.contrib.auth.models import User, Group
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from survey.survey.models import Person, PeerSurvey, ManagerSurvey

def get_persons(request):
  persons = Person.objects.all().values()
  person_list = list(persons)
  return JsonResponse(person_list, safe=False)

def person(request, id):
  obj = Person.objects.get(pk=id)
  data = serializers.serialize('json', [obj, ])
  struct = json.loads(data)
  data = json.dumps(struct[0]['fields'])
  return HttpResponse(data)

def get_peer_survey(request, id):
  obj = PeerSurvey.objects.get(pk=id)
  data = serializers.serialize('json', [obj, ])
  struct = json.loads(data)
  data = json.dumps(struct[0]['fields'])
  return HttpResponse(data)

def get_manager_survey(request, id):
  obj = ManagerSurvey.objects.get(pk=id)
  data = serializers.serialize('json', [obj, ])
  struct = json.loads(data)
  data = json.dumps(struct[0]['fields'])
  return HttpResponse(data)
