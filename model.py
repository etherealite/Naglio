from exlixir import *

import config
dbname = config.DATABASE['name']
metadata.bind = 'sqlite:///{dbname}'.format(dbname)


class Problem(Entity):
  service_name = Field(Unicode(60))
  acknowledged = Field(Boolean())
  active = Field(Boolean())
