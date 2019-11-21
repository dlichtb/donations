# API KEY:	386e293022889d02657232dad98494b8

import requests
from pprint import pprint

api_key = '386e293022889d02657232dad98494b8'

'''
headers = { "Authorization": "Bearer {api_key}" }
r = requests.get(	#AUTHENTICATION
					"https://api.pledgeling.com/v1/donations",
					# LIST ALL CUSTOMERS
					#"https://api.pledgeling.com/v1/customers",
					# RETRIEVE CUSTOMER DETAILS
					#"https://api.pledgeling.com/v1/customers/7adc74e8-caea-4faa-a660-27d39947921e",
  					headers=headers
  				)
pprint(r)
'''

# LIST ALL ORGANIZATIONS

import requests

headers = { "Authorization": "Bearer {api_key}" }
r = requests.get(
  "https://api.pledgeling.com/v1/organizations",
  headers=headers
  )
pprint(r)

# RETRIEVE ORGANIZATION DETAILS
'''
import requests

headers = { "Authorization": "Bearer {api_key}" }
r = requests.get(
  "https://api.pledgeling.com/v1/organizations/3685b542-61d5-45da-9580-162dca725966",
  headers=headers
  )
'''

# REQUEST AN ORGANIZATION
'''
import requests

headers = { "Authorization": "Bearer {api_key}" }
r = requests.post(
  "https://api.pledgeling.com/v1/organizations",
  data={
    "ngo_id": "58-2060131",
    },
  headers=headers
  )
  
# NOTE:	- Successful Response has a 202 Accepted status and empty body
'''


'''
# CREATE A CUSTOMER
headers = { "Authorization": "Bearer {api_key}" }
r = requests.post(
  "https://api.pledgeling.com/v1/customers/{id}",
  data={
    email: "yjh@ok.gov",
    first_name: "Yvonne",
    last_name: "Hilda",
    source: "tok_1Ev55hCfZhdqK156FfTmzPpQ"
    },
  headers=headers
  )
'''

'''
# UPDATE A CUSTOMER
headers = { "Authorization": "Bearer {api_key}" }
r = requests.patch(
  "https://api.pledgeling.com/v1/customers/b196c02b-e0b2-47cb-92f6-542753e73607",
  data={
    source: "tok_1Ev55hCfZhdqK156FfTmzPpQ"
    },
  headers=headers
  )
'''

'''
# DELETE A CUSTOMER
import requests

headers = { "Authorization": "Bearer {api_key}" }
r = requests.delete(
  "https://api.pledgeling.com/v1/customers/b196c02b-e0b2-47cb-92f6-542753e73607",
  headers=headers
  )
'''

# LIST ALL DONATIONS
'''
import requests

headers = { "Authorization": "Bearer {api_key}" }
r = requests.get(
  "https://api.pledgeling.com/v1/donations",
  headers=headers
  )
'''

# RETRIEVE DONATION DETAILS
'''
import requests

headers = { "Authorization": "Bearer {api_key}" }
r = requests.get(
  "https://api.pledgeling.com/v1/donations/0f69319c-9321-4531-ad52-6cb87a292d35",
  headers=headers
  )
'''

# CREATE A DONATION
'''
import requests

headers = { "Authorization": "Bearer {api_key}" }
r = requests.post(
  "https://api.pledgeling.com/v1/donations",
  data={
    "email": "yjh@ok.gov",
    "first_name": "Yvonne",
    "last_name": "Hilda",
    "organization_id": "dd959794-d83f-4128-be24-651d2a398f12",
    "amount": "0.68",
    "phone_number": "(918) 555-0188",
    "metadata": "shopify_id 870203745"
    },
  headers=headers
  )
'''

# RETRIEVE FUNDRAISER DETAILS
'''
import requests

headers = { "Authorization": "Bearer {api_key}" }
r = requests.get(
  "https://api.pledgeling.com/v1/fundraisers/9IEgDGbG9gMAEgFoKSvSpg",
  headers=headers
  )
'''

# CREATING A FUNDRAISER
'''
# Fundraiser with organization beneficiary and one organizer
import requests

headers = { "Authorization": "Bearer {api_key}" }
r = requests.post(
  "https://api.pledgeling.com/v1/fundraisers",
  data={
    "id": "9IEgDGbG9gMAEgFoKSvSpg",
    "start_time": "2019-05-04 03:00:00 UTC",
    "end_time": "2019-05-04 05:00:00 UTC",
    "goal": "1500.0",
    "beneficiary": {
      "type": "Organization",
      "id": "3685b542-61d5-45da-9580-162dca725966"
      },
    "organizers": [
      {
        "id": "okn6IpWQSNof_JWCMarFSw",
        "email": "sam@pledgeling.com",
        "first_name": "Sam",
        "last_name": "Goldstein"
        }
      ]
    },
  headers=headers
  )

##################################################################################

# Fundraiser with crowdfunding beneficiary and multiple organizers
import requests

headers = { "Authorization": "Bearer {api_key}" }
r = requests.post(
  "https://api.pledgeling.com/v1/fundraisers",
  data={
    "id": "7FEYuvnaeCTgQ8TuJkDsRQ",
    "start_time": "2019-05-05 00:00:00 UTC",
    "end_time": "2019-05-10 00:00:00 UTC",
    "goal": "3000.0",
    "beneficiary": {
      "type": "Crowdfund",
      "category": "Travel",
      "purpose": "Trip to Sweden"
      },
    "organizers": [
      {
        "id": "s660Z0wmdarLGgqp85oSdg",
        "email": "steve@pledgeling.com",
        "first_name": "Steve",
        "last_name": "Mansley"
        },
      {
        "id": "lwkV8LnEY9QMsprRI56BKw",
        "email": "margie@pledgeling.com",
        "first_name": "Margarette",
        "last_name": "Stewerdson"
        }
      ]
    },
  headers=headers
  )
'''

# UPDATE A FUNDRAISER
'''
import requests

headers = { "Authorization": "Bearer {api_key}" }
r = requests.post(
  "https://api.pledgeling.com/v1/fundraisers/{id}",
  data={
    "goal": "3000.0"
    },
  headers=headers
  )
'''

# PLACE A FUNDRAISER
'''
import requests

# Fundraiser with organization beneficiary and one organizer
import requests

headers = { "Authorization": "Bearer {api_key}" }
r = requests.post(
  "https://api.pledgeling.com/v1/fundraisers/{id}",
  data={
    "id": "9IEgDGbG9gMAEgFoKSvSpg",
    "start_time": "2019-05-04 03:00:00 UTC",
    "end_time": "2019-05-04 05:00:00 UTC",
    "goal": "1500.0",
    "beneficiary": {
      "type": "Organization",
      "id": "3685b542-61d5-45da-9580-162dca725966"
      },
    "organizers": [
      {
        "id": "s660Z0wmdarLGgqp85oSdg",
        "email": "steve@pledgeling.com",
        "first_name": "Steve",
        "last_name": "Mansley"
        },
      {
        "id": "lwkV8LnEY9QMsprRI56BKw",
        "email": "margie@pledgeling.com",
        "first_name": "Margarette",
        "last_name": "Stewerdson"
        }
      ]
    },
  headers=headers
  )
'''

# LIST ALL IMPACT CALCULATORS
'''
import requests

headers = { "Authorization": "Bearer {api_key}" }
r = requests.get(
  "https://api.pledgeling.com/v1/impact_calculators",
  headers=headers
  )
'''

# RETRIEVE IMPACT CALCULATOR DETAILS
'''
import requests

headers = { "Authorization": "Bearer {api_key}" }
r = requests.get(
  "https://api.pledgeling.com/v1/impact_calculators/",
  headers=headers
  )
'''

# CREATE AN IMPACT CALCULATOR
'''
import requests

headers = { "Authorization": "Bearer {api_key}" }
r = requests.post(
  "https://api.pledgeling.com/v1/impact_calculators",
  data={
    "icon": "clean-water",
    "color": "",
    "style": "",
    "currency_symbol": "",
    "external_id": "nil",
    "formula": "organization_amount",
    "description": "people provided with clean drinking water for one year",
    },
  headers=headers
  )
'''

# UPDATE AN IMPACT CALCULATOR
'''
import requests

headers = { "Authorization": "Bearer {api_key}" }
r = requests.patch(
  "https://api.pledgeling.com/v1/impact_calculators/AU9puRFzeJbU_EdMLoqwsA",
  data={
    "icon": "clean-water",
    "color": "#443a4a"
    },
  headers=headers
  )
'''
