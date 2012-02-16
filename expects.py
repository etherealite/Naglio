class Expects:
  """
  chain of rules a given response object is expected to match. Returns a
  list of failed and passed rules
  """
  def __init__(self, response, rules):
    self.response = response
    self.rules = rules
    self.failures = 0
    self.successes = 0

  def run_rules(self):
    for rule in self.rules:
      rule.evaluate(response)
      if rule



class ExpectsRule(object):
  pass


class StatusCode(ExpectsRule):
  def __init__(self, service_name, expects_code):
    self.service_name
    self.expects_code = expects_code
    self.evaluated = False
    self.depends = None
    self.passed = None  # pass or fail
    self.msg = None
    self.failtemp = "HTTP Status code was expected to be {} but the\
        service {} responded with {}"
    self.passtemp = "Reponse contained the expected HTTP status code {}"

  def evaluate(response):
    self.passed = False
    if response.status_code is self.expects_code:
      self.passed = True
      self.msg = self.failtemp.format(
          self.expects_code
          )
    if response.status_code is not self.expects_code:
      self.passed = False
      self.msg = failtemp.format(
          self.expects_code, service_name, response.status_code
          )
    else:
      raise Exception('something went wrong')
    self.evaluated = True


class Json(ExpectsRule):
  def __init(self):
    pass

