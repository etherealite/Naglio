#!/usr/bin/python2
import twilio.rest

from service import services

for service in services:
  if not service.problem:
    status = service.check()
    if status.issue:
      service.problem = status.issue
  if service.problems:
    problem = service.problem
    if not problem.acknowledged:
      problem.start_notify()
    status = service.check()
    if not status.issue:
      problem.end()


