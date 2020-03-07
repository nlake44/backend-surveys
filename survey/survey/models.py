import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Person for which we are doing the survey.
class Person(models.Model):
  first_name = models.CharField(max_length=64)
  last_name = models.CharField(max_length=64)
  email = models.EmailField(max_length=254)
  peers = models.ManyToManyField("self", blank=True)
  manager = models.ForeignKey("self",
                              null=True,
                              on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

# Top level survey model.
class Survey(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  person = models.ForeignKey(Person, on_delete=models.CASCADE)

# Peer survey model.
class PeerSurvey(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
  filled = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # Questions.
  values = models.IntegerField(null=True,
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  analytical = models.IntegerField(null=True,
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  execution = models.IntegerField(null=True,
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  leadership = models.IntegerField(null=True,
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  presence = models.IntegerField(null=True,
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  keep_doing = models.CharField(max_length=4096)
  stop_doing = models.CharField(max_length=4096)

# Manager survey model.
class ManagerSurvey(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
  filled = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # Questions.
  would_recommend = models.IntegerField(null=True,
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  opportunities = models.IntegerField(null=True,
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  communicates = models.IntegerField(null=True,
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  feedback = models.IntegerField(null=True,
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  priorities = models.IntegerField(null=True,
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  information = models.IntegerField(null=True,
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  expertise = models.IntegerField(null=True,
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  perspective = models.IntegerField(null=True,
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  decisions = models.IntegerField(null=True,
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  collaborates = models.IntegerField(null=True,
    validators=[MaxValueValidator(5), MinValueValidator(1)])
  keep_doing = models.CharField(max_length=4096)
  stop_doing = models.CharField(max_length=4096)


# API Keys for super admins.
class APIKey(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  person = models.ForeignKey(Person, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
