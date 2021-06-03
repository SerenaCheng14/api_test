import requests
from config.endpoints import *

#GET

r1 = requests.get(url=domain_beta + path_get, timeout=5)
print("Beta status: " + str(r1.status_code))

if r1.status_code == requests.codes.ok:
  print("Beta OK")
  print("Beta content:")
  print(r1.content)
  print("Beta headers:")
  print(r1.headers) 



r2 = requests.get(url=domain_production + path_get, timeout=5)
print("Production status: " + str(r2.status_code))

if r2.status_code == requests.codes.ok:
  print("Production OK")
  print("Production content:")
  print(r2.content)
  print("Production headers:")
  print(r2.headers) 


