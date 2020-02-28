from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from survey.survey.serializers import UserSerializer, GroupSerializer, PeerSurveySerializer, ManagerSurveySerializer, SurveySerializer, PersonSerializer


class UserViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Group.objects.all()
  serializer_class = GroupSerializer

class SurveyViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Group.objects.all()
  serializer_class = SurveySerializer

class PeerSurveyViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Group.objects.all()
  serializer_class = PeerSurveySerializer

class ManagerSurveyViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Group.objects.all()
  serializer_class = ManagerSurveySerializer

class PersonViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Group.objects.all()
  serializer_class = PersonSerializer
