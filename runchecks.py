#!/usr/bin/python2
import os
import sys
import urllib
import urllib2
import json
import time
import twilio.rest

import settings

services = settings.SERVICES

services = Build_Services(services)
for service in services:
  if service.problem:
    problem = service.problem
    if not problem.acknowledged:
      problem.start_notify()
    else:
      status = service.check()
      if not status.issue:
        problem.end
  else:
    status = service.check()
    if status.issue():
      service.problem = status.issue()

