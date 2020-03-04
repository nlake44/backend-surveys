from django.test import Client
from django.test import TestCase
from survey.survey.models import Person

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
