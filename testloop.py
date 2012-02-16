class Problem:
  pass

problem1 = Problem()
problem1.msg = "http status code needs to be 200 got 301"
problem2 = Problem()
problem2.msg = " there is fuckity derp problem"
problems = [problem1, problem2]

def sendcall():
  pass


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
    problems.pop()

