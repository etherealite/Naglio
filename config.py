"""
This is the configuration file for the script. 
"""
from os import environ, path
from config_tools import namedtupify


# Find dirname(full path to containing directory) of the project directory
mod_full = path.abspath(__file__)
mod_dirname = path.dirname(mod_full)

#
# Full Path to application directory
APP_PATH = mod_dirname

# Do debbuging stuff
DEBUG = True

# Domain for twilio callbacks.
DOMAIN = "http://3bpe.localtunnel.com"

# Twilio authentication
TWILIO = {
    'ACCOUNT_SID' : environ['ACCOUNT_SID'],
    'AUTH_TOKEN'  : environ['AUTH_TOKEN']
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
          'url' : 'https://tinypay.me/ping/server', 'timeout' : '1'
          }
      },
      'expects' : {
        'status_code': '200',
        'json' : {'match': { 'type' : 'server',  'up' : 'true' }}
        },
      'cycle_time' : 5
    }
}

