import time, random, logging
global twil_msg
twil_msg = 'somehit'

class AppRunner(object):

  def __init__(self, Service, contacts, acked, twil_msg):
    self.Service = Service
    self.contacts = contacts
    self.call_list = []
    self.problems = []
    self.acked = False


  def checkprobs(self):
    print "checking problems"
    self.Service.check()
    self.problems = self.Service.problems

    if self.problems:
      return self.checkacked
    else:
      return self.set_not_acked


  def checkacked(self):
    self.acked = acked
    if self.acked:
      return self.wait
    else:
      return self.makecall


  def set_not_acked(self):
    self.acked = False
    return self.wait


  def wait(self):
    time.sleep(5)
    return self.checkprobs


  def makecall(self):

    if len(self.call_list) <= 0:
      self.call_list = list(self.contacts)
      random.shuffle(self.call_list)
    callee = self.call_list.pop()
    print "contacting {} at {}".format(callee[0], callee[1]['phone'])
    print "using call back", config.DOMAIN + "/gather"
    self.call = client.calls.create(
        to=callee[1]['phone'],
        from_= config.TWILIO.CALL_FROM,
        url=config.DOMAIN + "/gather",
        method='GET',
        status_callback=config.DOMAIN + "/end",
        status_method='GET',
        if_machine = 'Hangup'
        )
    #blocking = ['QUEUED', 'RINGING', 'IN-PROGRESS']

    #return self.wait
    return


  def runme(self):
    self.call = None
    nextdo = self.checkprobs()
    while True:
      if hasattr(nextdo, "__call__"):
        nextdo = nextdo()
      else:
        break
