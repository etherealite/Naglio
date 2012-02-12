#!/usr/bin/python2
import os
import sys
import urllib
import urllib2
import json
import time
import twilio.rest

import settings

def servicecheck(url):
  try:
    f = urllib2.urlopen(url)
  except Exception, e:
    return 'can\'t reach json status service'
  resp = json.loads(f.read())
  pingtype = resp['type']
  up = resp['up']
  up = False
  if up is not True:
    return 'there is a problem with a service of type: %s' % pingtype
  else:
    return

def callisacked(callback):
  return False

def send_alert(person):
  # do some twilio stuff
  return 'callback'


def makecall(person, message):
  callback = send_alert(person)
  # calling person here
  if callisacked(callback):
    print person, 'acknowledged the error'
    print 'calling' , person, 'with message', message
  else:
    return

url = "https://tinypay.me/ping/server"
numbers = ['32399', '239852', '23498']
problem = False
acked = False
problem_msg = servicecheck(url)
if problem_msg and not acked:
  makecall('shithead', problem_msg)
time.sleep(3)


