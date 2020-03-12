from django.test import Client
from django.test import TestCase
from survey.survey.models import Person, Survey, PeerSurvey, ManagerSurvey, APIKey
import json

import logging
logging.disable(logging.CRITICAL)

class PersonTestCase(TestCase):
  def setUp(self):
    Person.objects.create(first_name="John",
                          last_name="Doe",
                          email="john@doe.com")
    person = Person.objects.create(first_name="Jane",
                                   last_name="Doe",
                                   email="jane@doe.com")
    APIKey.objects.create(person=person)

  def test_names(self):
    jane = Person.objects.get(first_name="Jane")
    john = Person.objects.get(first_name="John")
    self.assertEqual(jane.last_name, "Doe")
    self.assertEqual(john.last_name, "Doe")

  def test_person_list_url(self):
    jane = Person.objects.get(first_name="Jane")
    key = APIKey.objects.get(person=jane)
    c = Client()
    response = c.get('/persons', {'APIKEY': str(key.id)})
    self.assertEqual(response.status_code, 200)
    self.assertTrue("Jane" in str(response.content))
    self.assertTrue("John" in str(response.content))

  def test_person_list_url_with_bad_apikey(self):
    c = Client()
    response = c.get('/persons', {'APIKEY': 'badkey'})
    self.assertEqual(response.status_code, 403)

  def test_person_detail_url(self):
    jane = Person.objects.get(first_name="Jane")
    key = APIKey.objects.get(person=jane)
    c = Client()
    response = c.get('/person/1/', {'APIKEY': str(key.id)})
    self.assertEqual(response.status_code, 200)
    self.assertTrue("John" in str(response.content))

    response = c.get('/person/2/', {'APIKEY': str(key.id)})
    self.assertEqual(response.status_code, 200)
    self.assertTrue("Jane" in str(response.content))

  def test_person_detail_with_many_direct_reports(self):
    jane = Person.objects.get(first_name="Jane")
    john = Person.objects.get(first_name="John")
    jane.manager = john
    jane.save()
    key = APIKey.objects.get(person=jane)

    c = Client()
    response = c.get('/person/2/', {'APIKEY': str(key.id)})
    self.assertEqual(response.status_code, 200)
    json_obj = json.loads(response.content)
    self.assertTrue(john.id == json_obj["manager"])

    response = c.get('/person/1/', {'APIKEY': str(key.id)})
    self.assertEqual(response.status_code, 200)
    json_obj = json.loads(response.content)
    self.assertTrue(None == json_obj["manager"])

  def test_person_detail_with_peers(self):
    jane = Person.objects.get(first_name="Jane")
    john = Person.objects.get(first_name="John")
    jane.peers.add(john)
    key = APIKey.objects.get(person=jane)

    c = Client()
    response = c.get('/person/2/', {'APIKEY': str(key.id)})
    self.assertEqual(response.status_code, 200)
    json_obj = json.loads(response.content)
    self.assertTrue(john.id == json_obj["peers"][0])

    response = c.get('/person/1/', {'APIKEY': str(key.id)})
    self.assertEqual(response.status_code, 200)
    json_obj = json.loads(response.content)
    self.assertTrue(jane.id == json_obj["peers"][0])
 
  def test_person_detail_url_with_bad_key(self):
    c = Client()
    response = c.get('/person/1/', {'APIKEY': 'badkey'})
    self.assertEqual(response.status_code, 403)

    response = c.get('/person/2/', {'APIKEY': 'c63148a7-5455-48d3-ac33-59ae3508d9ad'})
    self.assertEqual(response.status_code, 403)

  def test_create_person(self):
    jane = Person.objects.get(first_name="Jane")
    key = APIKey.objects.get(person=jane)
    c = Client()
    raj = {'first_name': 'Raj',
           'last_name': 'Chohan',
           'email': 'nchohan@intouchhealth.com',
           'manager': 1,
           'peers': [2]
          }
    json_blob = json.dumps(raj)
    response = c.post('/createperson/',
                      {'APIKEY': str(key.id),
                       'data': json_blob
                      }
                     )
    self.assertEqual(response.status_code, 200)

    raj_verify = Person.objects.get(first_name="Raj")
    self.assertEqual(raj_verify.last_name, "Chohan")
    self.assertEqual(raj_verify.peers.all()[0], jane)

  def test_update_person(self):
    jane = Person.objects.get(first_name="Jane")
    key = APIKey.objects.get(person=jane)
    c = Client()
    jane = {'email': 'jane@doe.net',
            'id': jane.id
           }
    json_blob = json.dumps(jane)
    response = c.post('/createperson/',
                      {'APIKEY': str(key.id),
                       'data': json_blob
                      }
                     )
    self.assertEqual(response.status_code, 200)

class SurveyTestCase(TestCase):
  def setUp(self):
    person = Person.objects.create(first_name="John",
                                   last_name="Doe",
                                   email="john@doe.com")
    Survey.objects.create(person=person)

  def test_survey_get(self):
    person = Person.objects.get(first_name="John")
    survey = Survey.objects.get(person=person)
    self.assertEquals(survey.person.last_name, "Doe") 

class PeerSurveyTestCase(TestCase):
  def setUp(self):
    person = Person.objects.create(first_name="John", last_name="Doe", email="john@doe.com")
    survey = Survey.objects.create(person=person)
    PeerSurvey.objects.create(filled=False, survey=survey)

  def test_peer_survey_url(self):
    peer_survey = PeerSurvey.objects.get(filled=False)
    c = Client()
    response = c.get('/peersurvey/' + str(peer_survey.id) + '/')
    self.assertTrue(response.status_code, 200)
    self.assertTrue('keep_doing' in str(response.content))

class ManagerSurveyTestCase(TestCase):
  def setUp(self):
    person = Person.objects.create(first_name="John", last_name="Doe", email="john@doe.com")
    survey = Survey.objects.create(person=person)
    ms = ManagerSurvey.objects.create(filled=False, survey=survey)

  def test_manager_survey_url(self):
    manager_survey = ManagerSurvey.objects.get(filled=False)
    c = Client()
    response = c.get('/managersurvey/' + str(manager_survey.id) + '/')
    self.assertTrue(response.status_code, 200)
    self.assertTrue('keep_doing' in str(response.content))
