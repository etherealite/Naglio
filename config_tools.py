"""
tools to help read configuration config.py file.
"""

from collections import namedtuple
"""converts a dictionary into a named tuple.
:parm dic: the dcitionary to convert
:parm name: class name for the generated tuple.
"""
def namedtupify(dic, name):
  for k, v in dic.items():
    if isinstance(v, dict):
      dic[k] = namedtupify(v, k)
  Tupified = namedtuple(name, dic.keys())
  built_tuple = Tupified(**dic)
  return built_tuple
