"""
Response's are adaptors for the responses returned by Requester objects
that define a common interface for the restof the system and most
importantly, the rule chains of an Expects class
"""

from requester import GET
from urllib2 import HTTPError #URLError # not using yet...

class Response(object):
  """Response Adaptor
  :param raw_response: The response output of a Requester object
  :param requester: The Requester instance from which the raw_response
  came.
  :TODO get rid the requester instance required param laziness.
  possibly use descriptors
  """
  def __init__(self, raw_response, requester):
    self.raw_response = raw_response
    self.requester = requester
    self.followed_redirect = False
    self.url = None
    self.error = None
    self.status_code = None
    self.headers = None
    self.body = None

    # make sure that the requester supplied is of type
    # GET and get the non exception errors types that it
    # may have returned in instance of.
    RequestType = requester.__class__
    if RequestType is GET:
      self.non_exceptionals = RequestType.non_exceptionals
      self.process_raw_get_response()
    else:
      raise Exception(
          'the request type {} is not  implemented, only GET\
              is supported'.format (RequestType.__name__))

  def process_raw_get_response(self):
    """Process a raw get response.
    :TODO get rid of this method and institute something more
    dynamic.
    """
    non_excepts = self.non_exceptionals
    raw = self.raw_response

    #determine if a redirect was followed
    self.followed_redirect = False
    if self.requester.url is not raw.geturl():
      self.followed_redirect = True
    #if the raw respones is an urllib2 error act accordingly.
    if isinstance(raw, non_excepts):
      self.error = raw
      if isinstance(raw, HTTPError):
        self.status_code = raw.code
        self.headers = dict(raw.headers)
      else:
        #its a url error nothing to do
        pass

    else:
      #only urllib.addinfourl type should be now be possible
      self.status_code = raw.code
      self.headers = dict(raw.headers)
      self.body = raw.readlines()

