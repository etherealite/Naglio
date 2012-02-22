from requester import GET
from expects import Expects, StatusCode


class Service(object):
  """
  Contains service definition, runs checks on a service by executing
  a given request and passing in the response to an attached Expects
  instance.
  """

  def __init__(self, name, requester, expects):
    """
    set name of service, the request required to check the service's
    status, and the expectation instance to run the checks.
    """
    self.name = name
    self.requester = requester
    self.expects = expects

    self.problems = None

  def check(self):
    raw_response = self.requester.raw_response()
    response = ResponseCls(raw_response, self.requester)
    self.expects.run_rules(response)




def services(source):
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


