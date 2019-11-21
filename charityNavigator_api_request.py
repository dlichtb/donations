import requests, json, os
from pprint import pprint

#url = 'https://graphapi.firstgiving.com/v1/list/organization?q=government_id:260046127'
#url = 'https://demo.ckan.org/api/3/action/help_show?name=group_list'
#url = 'http://www.open.canada.ca/data/en/'
url = 'https://api.data.charitynavigator.org/v2'
#url = 'https://api.pledgeling.com/v1'

param = {	'app_id' : '448bb5cb',
			'app_key' : '75c79b9a39569f4006350e281893a440'}

response = requests.get(url, param)
#data = json.loads(response.status_code)
#print(data)
pprint(response.content)
