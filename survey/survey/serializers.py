from django.contrib.auth.models import User, Group
from survey.survey.models import Person, Survey, PeerSurvey, ManagerSurvey
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ['url', 'name']

class PersonSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Person
    fields = ['first_name', 'last_name', 'email', 'direct_reports', 'peers']

class SurveySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Survey
    fields = ['filled', 'creation_date', 'last_updated']

class PeerSurveySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = PeerSurvey
    fields = ['id', 'survey', 'person', 'values', 'analytical', 'execution', 'leadership', 'presence', 'keep_doing', 'stop_doing']

class ManagerSurveySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = ManagerSurvey
    fields = ['id', 'survey', 'person', 'would_recommend', 'opportunities', 'communicates', 'feedback', 'priorities', 'information', 'expertise', 'perspective', 'decisions', 'collaborates', 'keep_doing', 'stop_doing']
