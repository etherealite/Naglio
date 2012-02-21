import time, threading, random
from bottle import route, run
from twilio import twiml


@route('/msg')
def saymsg():
  press1 = " To acknowledge this message press 1 now"
  r = twiml.Response()
  r.say(press1)
  r.gather(finishOnKey=1)
  r.redirect(config.DOMAIN + '/ack')
  return str(r)


@route('/ack')
def ack():
  global acked
  acked = True
  r = twiml.Response()
  r.say('Thank and good bye.')
  r.hangup()
  return str(r)


@route('/failed')
def failed():
  r = twiml.Response()
  if len(numbers) is 0:
    calling = False
    r.hangup()
  else:
    calling_num = numbers.pop(0, len(numbers) - 1)
    print 'initing call {}'.format(calling_num)



kw_args = {'server': 'tornado', 'host':'localhost', 'port':8080}
t = threading.Thread(target=run, kwargs=kw_args)
t.daemon = True
t.start()


class Problem:
  pass

def makemeproblems():
  problem1 = Problem()
  problem1.msg = "http status code needs to be 200 got 301"
  problem2 = Problem()
  problem2.msg = " there is fuckity derp problem."
  problems = [problem1, problem2]
  return problems

problems = makemeproblems()
calling = False
acked = False
numloops = 0
while True:
  if problems and not acked:
    numbers = ['phone1', 'phone2', 'phone3']
    msg = "there is a problem, "
    first_msg = True
    for problem in problems:
      if not first_msg:
        msg += " and " + problem.msg
      else:
        first_msg = False
        msg += problem.msg
    num_problems = len(problems)
    calling_num = numbers.pop(random.randint(0, len(numbers) - 1))
    print "initiating call to number {}".format(calling_num)
    #problems.pop()
  else:
    msg = "no problems reported"
  time.sleep(3)
  print 'is acked? ', acked
  numloops += 1
  print 'time through', numloops
  if numloops is 5:
    problems = []
  if not problems:
    acked = False
