"""
This code reads a lot better when I know what it does.
-In memory of Michael Karpeles
"""
import config
from urllib2 import urlopen, HTTPError, URLError
import json
import sys
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



def reqfactory(request_dic):
  action = request_dic['action']
  options = request_dic['options']
  ReqClass = globals()[action]
  requester = ReqClass(options)
  return requester






class GET(object):
  """
  Abstraction of as simple get request
  """
  def __init__(self, options):
    self.url = options['url']
    self.timeout = int(options['timeout'])
    self.sender = urlopen

  def __call__(self):
    return self.sender(self.url, None, self.timeout)


class Expects:
  """
  chain of expections of a given response object and returns a list
  of failed checks.
  """
  def __init__(self, response):
    self.response = response


class ExpectsRule:
  def __init__(self):
    pass

def services(source=config.SERVICES):
    """
    This code reads a lot better when I know what it does.
    -Michael Karpeles
    """
    for service_name, definition in source.items():
      request_dict =  definition['request']

      request = GET(action['ur'], action['timeout'])
      expects = None
      #expects_dict = definition['expects']
      service = Service(service_name, request, expects)
      yield service

myrequest = reqfactory(config.SERVICES['server_ping']['request'])
