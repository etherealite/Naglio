"""
Response's are adaptors for the responses returned by Requester objects
that define a common interface for the restof the system and most
importantly, the rule chains of an Expects class
"""

from requester import GET
from urllib2 import HTTPError #URLError # not using yet...

class Response(object):
  """Response Adaptor
  Takes a raw response froma Requester object and format it to a
  structure readable by an Excpects object.
  """
  def __init__(self, raw_response, RequestType):
    self.raw_response = raw_response
    self.url = None
    self.error = None
    self.headers = None
    self.body = None
    self.status_code = None

    if RequestType is GET:
      self.non_exceptionals = RequestType.non_exceptionals
      self.process_get_response()
    else:
      raise Exception(
          'the request type {} is not  implemented, only GET\
              is supported'.format (RequestType.__name__))

  def process_get_response(self):
    """
    TODO: get rid of this method and institute something more
    dynamic.
    """
    non_excepts = self.non_exceptionals
    raw = self.raw_response
    if isinstance(raw, non_excepts):
      self.error = raw
      if isinstance(raw, HTTPError):
        self.status_code = raw.code
        self.headers = dict(raw.headers)
      else:
        """its a url error nothing to do"""
        pass

    else:
      """only urllib.addinfourl type should be now be possible"""
      self.status_code = raw.code
      self.url = raw.geturl()
      self.headers = dict(raw.headers)
      self.body = raw.readlines()

