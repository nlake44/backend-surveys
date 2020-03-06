import json
from django.core import serializers
from django.contrib.auth.models import User, Group
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from survey.survey.models import Person, PeerSurvey, ManagerSurvey
from survey.survey.helpers import requires_api_key

@requires_api_key
@require_http_methods(["GET"])
def get_persons(request):
  persons = Person.objects.all().values()
  person_list = list(persons)
  return JsonResponse(person_list, safe=False)

@requires_api_key
@require_http_methods(["GET"])
def person(request, id):
  obj = Person.objects.get(pk=id)
  data = serializers.serialize('json', [obj, ])
  struct = json.loads(data)
  data = json.dumps(struct[0]['fields'])
  return HttpResponse(data)

@require_http_methods(["GET", "POST"])
def peer_survey(request, id):
  if request.method == 'GET':
    return __get_peer_survey(request, id)
  elif request.method == 'POST':
    return __post_peer_survey(request, id)
  else:
    return HttpResponseNotFound('<h1>Page was not found</h1>')

@require_http_methods(["GET", "POST"])
def manager_survey(request, id):
  if request.method == 'GET':
    return __get_manager_survey(request, id)
  elif request.method == 'POST':
    return __post_manager_survey(request, id)
  else:
    return HttpResponseNotFound('<h1>Page was not found</h1>')

def __get_manager_survey(request, id):
  obj = ManagerSurvey.objects.get(pk=id)
  data = serializers.serialize('json', [obj, ])
  struct = json.loads(data)
  data = json.dumps(struct[0]['fields'])
  return HttpResponse(data)

def __post_manager_survey(request, id):
  obj = PeerSurvey.objects.get(pk=id)
  struct = json.loads(request.content)
  print(struct)
  return HttpResponse("{'success': 'true'}")
def __post_peer_survet(request, id):
  obj = PeerSurvey.objects.get(pk=id)
  struct = json.loads(request.content)
  print(struct)
  return HttpResponse("{'success': 'true'}")

def __get_peer_survey(request, id):
  obj = PeerSurvey.objects.get(pk=id)
  data = serializers.serialize('json', [obj, ])
  struct = json.loads(data)
  data = json.dumps(struct[0]['fields'])
  return HttpResponse(data)

