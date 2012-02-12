import config
import urllib2


class Service(object):
  """
  Contains service definition, checking actions and stuff
  """
  def __init__(self, name, request, expects):
    """
    set name of service, check if there are existing problems for
    service
    """
    self.name = name
    self.request = request
    self.expects = expects
    self.problem = None

  def check(self):
    try:
      response = self.request()
    except (HTTPError, URLError) as inst:
      response = inst
    self.expects(response)

    status = None
    return status


class Request:
  pass

class GET(Request):
  def __init__(self, url, timeout=None):
    self.timeout = timeout
    self.action = urllib2.urlopen

  def __call__(self):
    self.send(url, None, timeout)

class Excpects:
  def __init__(self):
    self.
def services(self, source=config.SERVICES)
    """
    This code reads a lot better when I know what it does.
    """
    for name, definition in source:
      request_dict = definition['request']
      response_dict = definiton['response']

      request = Request()
      request.action = request_dic['action']
      request.a

      service = Service(name)
      yield service


