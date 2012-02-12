import os
import sys
import time

# Find dirname of project directory
mod_full = os.path.abspath(__file__)
mod_dirname = os.path.dirname(mod_full)

# Full Path to application directory
APP_PATH = mod_dirname

# Do debbuging stuff
DEBUG = True

# Domain for twilio callbacks.
DOMAIN = "www.something.com"

# Database settings go here
DATABASE = {
    'host': None,
    'user': None,
    'name': 'ping.db',
    'port': None
    }

# List of people to notify on problems
CONTACTS = {
    'Evan' : {'phone' : 4152724198},
    'Dan'  : {'phone' : 2342342341}
    }

# Services to be checked and generate new problem events
SERVICES = {
    'server_ping' : {
      'request'  : {
        'action' : 'GET',
        'options' : {
          'url' : 'https://tinypay.me/ping/server', 'timeout' : '15'
          }
      },
      'expects' : {
        'status_code': '200',
        'json' : 'match': { 'type' : 'server',  'up' : 'true' }
        }
    }
}

