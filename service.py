import config
from urllib2 import urlopen, HTTPError, URLError
import json

class Service(object):
  """
  Contains service definition, runs checks on a service by executing
  a given request and passing in the request to an expects instance.
  """
  def __init__(self, name, request, expects):
    """
    set name of service, the request required to check the service's
    status, and the expectation instance to run the checks.
    """
    self.name = name
    self.request = request
    self.expects = expects

"""
  # safe keeping at the moment.
  def get_problem(self):
    name = self.name
    acknowledged = 0
    kwargs = {
        'active' : 1,
        'service_name' : self.name
        'issue'
        }
    problem = Problem.query.filter_by(**kwargs).one()
    return problem
"""


  def check(self):
    """
    check the service to make sure that the response returned by
    it's request meets expectaions.
    """
    try:
      response = self.request()
    except (HTTPError, URLError) as inst:
      response = inst
    #self.expects(response)
    return response



class Request:
  """
  base request object with which to build request abstractions.
  """
  pass

class GET(Request):
  """
  Abstraction of a get request
  """
  def __init__(self, url, timeout=None):
    self.url = url
    self.timeout = timeout
    self.send = urlopen

  def __call__(self):
    return self.send(self.url, None, self.timeout)


class Expects:
  """
  chain of expections of a given response object and returns a list
  of failed checks.
  """
  def __init__(self, response):
    self.response = response



def services(source=config.SERVICES):
    """
    This code reads a lot better when I know what it does.
    -Michael Karpeles
    """
    for service_name, definition in source.items():
      request_dict =  definition['request']
      if not request_dict['action'] is not 'GET':
        raise 'only \GET\' request is implemented'
      action = requst_dict['action']

      request = GET(action['ur'], action['timeout'])
      expects = None
      #expects_dict = definition['expects']
      service = Service(service_name, request, expects)
      yield service

myget = GET('http://google.com:32987', 1)
myservice = Service('myservice', myget, None)

