import json
import sys
class Expects:
  """
  chain of rules a given response object is expected to match. Returns a
  list of failed and passed rules
  """
  def __init__(self, rules):
    self.rules = rules
    self.reset()

  def reset(self):
    self.rules_evaluated = False
    self.failures = []
    self.successes = []

  def runrules(self, response):
    global failures
    failures = []
    global successes
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
    self.passed = None
    self.msg = None

  def check_depends(self):
    """check for the dependancies
    :Note only supports a single dependancy for Json class
    """
    self.depfail = True
    global successes
    for rule in successes:
      cls = self.depends[0][0]
      args = self.depends[0][1]
      if isinstance(rule, cls):
        if rule.expects_code is args and rule.passed:
            self.depfail = False
            return


  def evaluate(self, response=None):
    self.check_depends()
    if self.depfail is True:
      self.msg = "Failed due to a rule chain dependancy"
      self.passed = False



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
      self.msg = self.failtemp.format(
          self.expects_code, response.status_code
          )
    else:
      raise Exception('something went wrong')
    self.evaluated = True


class Json(ExpectsRule):
  def __init__(self, comparisons=None):
    super(Json, self).__init__()
    self.comparisons = comparisons
    self.failtemp = "Key values: {} were expected but, ".format(
        comparisons)
    self.depends =((StatusCode, 200),)

  def evaluate(self, response):
    super(Json, self).evaluate()
    if self.depfail is True:
      self.msg = "Depended on status code being 200"
      return
    self.msg = self.failtemp
    body = response.body
    resp_dic = json.loads(body)
    if not resp_dic:
      self.passed = False
      self.msg = "response was not valid json"
      return

    if self.comparisons:
      passed = True
      comparisons = self.comparisons
      deltas = {}
      keys_missing = []
      for key, value in comparisons.items():
        if not resp_dic.has_key(key):
          keys_missing.append(key)
          continue
        if resp_dic[key] != value:
          deltas[key] = resp_dic[key]

      if len(keys_missing):
        print len(keys_missing)
        self.msg += "keys {} were missing".format(", ".join(keys_missing))
        passed = False

      if len(deltas):
        if len(keys_missing):
          self.msg += ", and "
        self.msg += "the following key values didn't match {}".format(
            deltas)
        passed = False

    if passed:
      self.passed = True
      self.msg = "Passed"

