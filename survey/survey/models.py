import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Person for which we are doing the survey.
class Person(models.Model):
  first_name = models.CharField(max_length=64)
  last_name = models.CharField(max_length=64)
  email = models.EmailField(max_length=254)
  peers = models.ManyToManyField("self")
  direct_reports = models.ManyToManyField("self")

# Top level survey model.
class Survey(models.Model):
  filled = models.BooleanField(default=False)
  creation_date = models.DateField()
  last_updated = models.DateField()

# Peer survey model.
class PeerSurvey(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
  person = models.ForeignKey(Person, on_delete=models.CASCADE)

  # Questions.
  values = models.IntegerField(
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  analytical = models.IntegerField(
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  execution = models.IntegerField(
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  leadership = models.IntegerField(
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  presence = models.IntegerField(
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  keep_doing = models.CharField(max_length=4096)
  stop_doing = models.CharField(max_length=4096)

# Manager survey model.
class ManagerSurvey(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
  person = models.ForeignKey(Person, on_delete=models.CASCADE)

  # Questions.
  would_recommend = models.IntegerField(
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  opportunities = models.IntegerField(
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  communicates = models.IntegerField(
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  feedback = models.IntegerField(
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  priorities = models.IntegerField(
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  information = models.IntegerField(
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  expertise = models.IntegerField(
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  perspective = models.IntegerField(
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  decisions = models.IntegerField(
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  collaborates = models.IntegerField(
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  keep_doing = models.CharField(max_length=4096)
  stop_doing = models.CharField(max_length=4096)
