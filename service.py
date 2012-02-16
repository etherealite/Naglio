"""
"This code reads a lot better when I know what it does." -Michael Karpeles
"""
import json
import sys

from config_tools import namedtupify
import config
from requester import *

SERVICES = namedtupify(config.SERVICES, 'Services')

class Service(object):
  """
  Contains service definition, runs checks on a service by executing
  a given request and passing in the response to an attached Expects
  instance.
  """

  def __init__(self, name, requester, Response, expects):
    """
    set name of service, the request required to check the service's
    status, and the expectation instance to run the checks.
    """
    self.name = name

    self.requester = requester
    self.raw_response = None

    self.response = None
    self.expects = expects
    self.problem = None

  def check(self):
    pass



def services(source=config.SERVICES):
    """
    Factory to generate Service objects from 'source' configuration
    namedtuple.
    """
    for service_name, definition in source.items():
      request_dict =  definition['request']

      request = GET(action['ur'], action['timeout'])
      expects = None
      #expects_dict = definition['expects']
      service = Service(service_name, request, expects)
      yield service


#myrequest = request(SERVICES.server_ping.request)
myrequest = GET('http://google.com', 1)
myresponse = Response(myrequest(), GET)
