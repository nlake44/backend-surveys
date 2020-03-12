from survey.survey.models import APIKey
from django.core.exceptions import PermissionDenied
from uuid import UUID

import logging
logger = logging.getLogger(__name__)

""" Helper methods for views. """
def requires_api_key(function):
  def _inner(request, *args, **kwargs):
    key = request.GET.get('APIKEY', None) or request.POST.get('APIKEY')
    if key == None:
      logger.error("No API key supplied")
      raise PermissionDenied
    try:
      uuid_obj = UUID(key, version=4)
    except ValueError:
      logger.error("Bad key:" + str(key))
      raise PermissionDenied

    try:
      key_object = APIKey.objects.get(pk=key)
    except APIKey.DoesNotExist:
      raise PermissionDenied
    return function(request, *args, **kwargs)
  return _inner
