from django.test import Client
from django.test import TestCase
from survey.survey.models import Person, Survey, PeerSurvey, ManagerSurvey

class PersonTestCase(TestCase):
  def setUp(self):
    Person.objects.create(first_name="John", last_name="Doe", email="john@doe.com")
    Person.objects.create(first_name="Jane", last_name="Doe", email="jane@doe.com")

  def test_names(self):
    jane = Person.objects.get(first_name="Jane")
    john = Person.objects.get(first_name="John")
    self.assertEqual(jane.last_name, "Doe")
    self.assertEqual(john.last_name, "Doe")

  def test_person_url(self):
    c = Client()
    response = c.get('/persons')
    self.assertEqual(response.status_code, 200)
    self.assertTrue("Jane" in str(response.content))
    self.assertTrue("John" in str(response.content))

class SurveyTestCase(TestCase):
  def setUp(self):
    person = Person.objects.create(first_name="John", last_name="Doe", email="john@doe.com")
    Survey.objects.create(person=person)
    Survey.objects.create(person=person)

  def test_survey_url(self):
    pass 

class PeerSurveyTestCase(TestCase):
  def setUp(self):
    person = Person.objects.create(first_name="John", last_name="Doe", email="john@doe.com")
    survey = Survey.objects.create(person=person)
    PeerSurvey.objects.create(filled=False, survey=survey)

  def test_peer_survey_url(self):
    pass 

class ManagerSurveyTestCase(TestCase):
  def setUp(self):
    Survey.objects.create(filled=True)
    Survey.objects.create(filled=False)
    ManagerSurvey.objects.create()
    ManagerSurvey.objects.create()
