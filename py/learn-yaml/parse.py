#!/usr/bin/python2.7

import pyaml
import yaml
import pprint as pp

content = None

with open("a.yml") as f:
  content = yaml.load(f.read())
  print content.keys()
  
def load(key):
  config = content
  for k in key.split("."):
    if config:
      config = config.get(k)
    else:
      break
  return config

def pretty(kvs, size=2):
  lvl, _size = 0, size
  indent = " " * _size
  for kv in kvs:
    print indent * lvl + kv
  

print load("spring.data-source.host")
print load("spring.data-source.port")
print load("spring.data-source.timeout")
print load("what the: fuck")
print load("key with spaces")
print load("null_value")
print load("fucked up block").strip(), "#"
print load("another messed up")
print load("spring.version")
print load("true")
print load("man utd")
print load("real madrid")

pp.pprint(content)