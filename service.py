
"""
"This code reads a lot better when I know what it does."
-Michael Karpeles
"""
#from service import Service
from requester import GET
from expects import Expects, StatusCode, Json

class ServerPing(object):
  name = "Tiny Pay Server Ping"
  requester = GET('https://tinypay.me/ping/server', 1)
  rules = [StatusCode(200), Json({u'type':u'server', u'up':True})]
  expects = Expects(rules)
  problems = []
  msg = "starting up"
  @classmethod
  def check(cls):
    cls.requester.sendrequest()
    cls.expects.runrules(cls.requester)
    cls.problems = cls.expects.failures

    if cls.problems:
      cls.msg = "{} has detected problems:\n".format(cls.name)
      probnum = 1
      for failure in cls.problems:
        cls.msg += "Problem number {}, {}, ".format(probnum, failure.__class__.__name__)
        cls.msg += failure.msg
        cls.msg += ".\n"
        probnum += 1
    else:
      cls.msg = "{}, all system go.".format(cls.name)

if __name__ == '__main__':
  ServerPing.check()
  print ServerPing.problems
  print ServerPing.msg
