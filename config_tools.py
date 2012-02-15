"""
tools to help read configuration
"""

from collections import namedtuple
"""
converts a dictionary into a set of named tuples.
"""
def namedtupify(dic, name=None):
  for k, v in dic.items():
    if isinstance(v, dict):
      dic[k] = namedtupify(v, k)
  Tupified = namedtuple(name, dic.keys())
  built_tuple = Tupified(**dic)
  return built_tuple






