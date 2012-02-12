import os
import sys
import time
import twilio.rest





mod_full = os.path.abspath(__file__)
mod_dirname = os.path.dirname(path)

# Full Path to application directory
APP_PATH = mod_dirname

DEBUG = True

# Domain for twilio callbacks.
DOMAIN = "www.something.com"

# Database settings go here
DATABASE = {
    'host': None,
    'user' : None,
    'name' : 'ping.db',
    'port' : None
    }


# List of people to notify on problems
CONTACTS = {
    'matt' : {'phone' : 4154154150},
    'Doug' : {'phone' : 2342532523}
    }


# services to be checked and generate new problem events
SERVICES = {
    'server_ping' : {
      'request' : 'get_url' : {'url' : 'https://tinypay.me/ping/server'},
      'response' : 'json' : { 'type' : 'server',  'up' : 'true' }
}



