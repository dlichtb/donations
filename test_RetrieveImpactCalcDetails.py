import requests, os, sys
from pprint import pprint

api_key = "386e293022889d02657232dad98494b8"

endpoint_donations = "https://api.pledgeling.com/v1/donations"
endpoint_ListAllOrganizations = "https://api.pledgeling.com/v1/organizations"
endpoint_ListAllOrganizations_page2 = "https://api.pledgeling.com/v1/organizations?page=2"
endpoint_RetrieveImpactCalculatorDetails = "https://api.pledgeling.com/v1/impact_calculators/"

'''
headers = { "Authorization": "Bearer {api_key}" }
r = requests.get(
  "https://api.pledgeling.com/v1/donations",
  headers=headers
  )
pprint(r)
'''

#cmd_auth = os.system("curl {} -H 'Authorization: Bearer {}'".format(endpoint_donations, api_key))

cmd_ListAllOrganizations = os.system("curl {} -H 'Authorization: Bearer {}'".format(endpoint_ListAllOrganizations, api_key))
cmd_ListAllOrganizations = os.system("curl {} -H 'Authorization: Bearer {}'".format(endpoint_ListAllOrganizations_page2, api_key))
cmd_RetrieveImpactCalculatorDetails = os.system("curl {} -H 'Authorization: Bearer {}'".format(endpoint_RetrieveImpactCalculatorDetails, api_key))
#pprint(cmd_auth)
#pprint(cmd_ListAllOrganizations)
#pprint(endpoint_ListAllOrganizations_page2)
pprint(cmd_RetrieveImpactCalculatorDetails)
