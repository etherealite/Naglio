import time, random, sys, logging
from threading import Thread

# 3rd party
from twilio.rest import TwilioRestClient
from twilio import twiml
from bottle import route, run

# Internal libs
import config
global config
from config_tools import namedtupify
from service import ServerPing
from webface import *
from apprunner import AppRunner


config.TWILIO = namedtupify('Config', config.TWILIO)
client = TwilioRestClient(
    config.TWILIO.ACCOUNT_SID, config.TWILIO.AUTH_TOKEN)

@route('/')
def index():
  global twil_msg
  return twil_msg


@route('/gather')
def gather():
  global twil_msg
  press1 = " To acknowledge this message press 1 and then the # now."
  twil_msg += press1
  r = twiml.Response()
  r.say(twil_msg)
  r.gather(action=config.DOMAIN + '/ack', finishOnKey="#", method="GET")
  #r.redirect(config.DOMAIN + '/ack')
  return str(r)


@route('/ack')
def ackdo():
  global acked
  acked = True
  r = twiml.Response()
  r.say('Thank you and good bye.')
  r.hangup()
  return str(r)

@route('/end')
def ending():
  sys.exit()

@route('/fail')
def callfail():
  # release lock here
  pass


def bottlerunner():
  run(host='localhost', port=8080)


if __name__ == '__main__':

  global twil_msg
  twil_msg = "starting up"

  global acked
  acked = False

  pingapp = AppRunner(ServerPing, config.CONTACTS, acked, twil_msg)

  pingapp.checkprobs()
  print pingapp.Service.msg



  m = Thread(target=bottlerunner())
  m.daemon = True
  m.start()
  #s = Thread(target=pingapp.runme())
  #s.daemon = True
  #s.start()

