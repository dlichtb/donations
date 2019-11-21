import requests, os, sys
from pprint import pprint

api_key = "386e293022889d02657232dad98494b8"
endpoint_donations = "https://api.pledgeling.com/v1/donations"

'''
headers = { "Authorization": "Bearer {api_key}" }
r = requests.get(
  "https://api.pledgeling.com/v1/donations",
  headers=headers
  )
pprint(r)
'''

cmd_auth = os.system("curl {} -H 'Authorization: Bearer {}'".format(endpoint_donations, api_key))
pprint(cmd_auth)
