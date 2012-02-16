"""
Requesters are an encapsulation of the more fundamental components.
of building an object to perform request on remote services.
"""


from urllib2 import urlopen, HTTPError, URLError

class Requester(object):
  """Base class to build new types of Requester classes
  :TODO set a meta class on this to build a registry
  """
  pass


class GET(Requester):
  """ Abstraction of as simple get request
  :param url: the url in which to make the request
  :param timeout: the timeout for the request in seconds.
  :Note This request will follow redirects without exception
  """
  non_exceptionals = (HTTPError, URLError)
  def __init__(self, url, timeout=1):
    self.url = url
    self.timeout = 1
    request_sent = False
    self.raw_response = None
    self.opener = urlopen

  def sendrequest(self):
    """send the request and return the response.
    :Note urllib2 throws an exception for all http errorcodes which
    in this context are not 'exceptional'.
    """
    try:
      raw_response = self.opener(self.url, None, self.timeout)
    except self.non_exceptionals as excep_resp:
      raw_response = excep_resp
    self.raw_response = raw_response
    self.request_sent = True

  def __call__(self):
    self.sendrequest()
    return self.raw_response


def request(config):
  """create a Requester object from config
  :param config: a namedtuple with action and options attributes.
  :TODO clarify required structure of 'config' parameter.
  """
  action = config.action
  options = config.options._asdict()
  classes = {'GET':GET}
  RequesterClass = classes[action]
  requester = RequesterClass(**options)
  return requester


myget = GET('http://google.com')

