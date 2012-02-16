from threading import Thread
import time
import webface



kw_args = {'host':'localhost', 'port':8080}
t = Thread(target=webface.run, kwargs=kw_args)
t.daemon = True
t.start()

class Problem:
  pass

problem1 = Problem()
problem1.msg = "http status code needs to be 200 got 301"
problem2 = Problem()
problem2.msg = " there is fuckity derp problem"
problems = [problem1, problem2]



while True:
  team = ['4152724198', '4152734545']
  if problems:
    msg = "there is a problem, "
    first_msg = True
    for problem in problems:
      if not first_msg:
        msg += " and " + problem.msg
      else:
        first_msg = False
        msg += problem.msg
    webface.problems = len(problems)
    webface.message = msg
    problems.pop()
    print msg
  else:
    webface.problems = 0
    webface.message = "no problems reported"
    del t
  time.sleep(3)

