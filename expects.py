import json

class Expects:
  """
  chain of rules a given response object is expected to match. Returns a
  list of failed and passed rules
  """
  def __init__(self, rules):
    self.rules = rules
    self.rules_evaluated = False
    self.failures = []
    self.successes = []

  def run_rules(self, response):
    failures = []
    successes = []
    for rule in self.rules:
      rule.evaluate(response)
      if rule.passed is False:
        failures.append(rule)
      else:
        successes.append(rule)
    self.failures = failures
    self.successes = successes


class ExpectsRule(object):
  def __init__(self):
    """Shared attributes
    descendents should implement rules based on these attributes
    """
    self.evaluated = False
    self.depends = None
    self.depfail = None
    self.passed = None  # pass or fail
    self.msg = None
    self.check_depends()

  def check_depends(self):
    """check for the dependancies
    :Note only supports a single dependancy
    """
    self.depfail = True
    global successes
    for rule in successes:
      cls = self.depends[0][0]
      args = self.depends[0][1]
      if isinstance(rule, cls) 
        if rule.expects_code = args:
          if rule.passed:
            self.depfail = False
    if self.depfail is True:
      self.msg = "Failed due to a rule chain dependancy"


  def evaluate(self, response):
    raise Exception('not implemented')



class StatusCode(ExpectsRule):
  def __init__(self, expects_code):
    self.expects_code = expects_code
    self.failtemp = "HTTP Status code was expected to be {} but\
        it was {}"
    super(StatusCode, self).__init__()


  def evaluate(self, response):
    self.passed = False
    if response.status_code is self.expects_code:
      self.passed = True
      self.msg = "Passed"
    elif response.status_code is not self.expects_code:
      self.passed = False
      self.msg = failtemp.format(
          self.expects_code, service_name, response.status_code
          )
    else:
      raise Exception('something went wrong')
    self.evaluated = True


class Json(ExpectsRule):
  def __init__(self, comparisons):
    self.comparisons = comparisons
    self.failtemp = "Key values: {} were expected but {}"
    self.depends =((StatusCode, 200),)
    super(Json, self).__ini__()



