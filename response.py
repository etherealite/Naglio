"""
Response's are adaptors for the responses returned by Requester objects
that define a common interface for the restof the system and most
importantly, the rule chains of an Expects class
"""


class Response(object):
  pass


class UrlLibHTTP(Response):
  """Response Adaptor
  Mixin for Requesters that retun a response from the base urlopen in
  urllib2 in the python standerd library.
  """
  def reset(self):
    """Null out the processed response
    """
    self.error = None
    self.status_code = None
    self.headers = None
    self.body = None


  def process_raw_response(self):
    """Process a raw get response.
    :TODO get rid of this method and institute something more
    dynamic.
    """
    non_excepts = self.non_exceptionals
    raw = self.raw_response

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
      self.body = "".join(raw.readlines())


