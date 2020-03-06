from survey.survey.models import APIKey
from django.core.exceptions import PermissionDenied
from uuid import UUID

""" Helper methods for views. """
def requires_api_key(function):
  def _inner(request, *args, **kwargs):
    key = request.GET.get('APIKEY', None)
    if key == None:
      raise PermissionDenied

    try:
      uuid_obj = UUID(key, version=4)
    except ValueError:
      raise PermissionDenied

    key_object = APIKey.objects.get(pk=key)
    if key_object == None:
      raise PermissionDenied
    return function(request, *args, **kwargs)
  return _inner
