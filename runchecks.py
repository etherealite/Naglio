#!/usr/bin/python2

services = Services()

services = Build_Services(services)
for service in services:
  if not service.problem:
    status = service.check()
    if status.issue:
      service.problem = status.issue
  if service.problem:
    problem = service.problem
    if not problem.acknowledged:
      problem.start_notify()
    status = service.check()
    if not status.issue:
      problem.end()


