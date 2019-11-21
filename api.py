import os
from pprint import pprint

'''
	REFS:
		- https://developer.signupgenius.com/developer/keybaseddocs#/
'''

'''
#cmd1 = os.system("curl -X GET --header 'Accept: application/json' 'https://api.signupgenius.com/v2/k/user/profile/?user_key=V0FzMkxZcmVOZlVnclZMVEl6dGhWQT09'")
#cmd2 = os.system("curl -X GET --header 'Accept: application/json' 'https://api.signupgenius.com/v2/k/groups/_key=V0FzMkxZcmVOZlVnclZMVEl6dGhWQT09'")
#cmd3 = os.system("curl -X GET --header 'Accept: application/json' 'https://api.signupgenius.com/v2/k/user/profile/?user_key=V0FzMkxZcmVOZlVnclZMVEl6dGhWQT09'")
#cmd4 = os.system("curl -X GET --header 'Accept: application/json' 'https://api.signupgenius.com/v2/k/user/profile/?user_key=V0FzMkxZcmVOZlVnclZMVEl6dGhWQT09'")
#cmd5 = os.system("curl -X GET --header 'Accept: application/json' 'https://api.signupgenius.com/v2/k/user/profile/?user_key=V0FzMkxZcmVOZlVnclZMVEl6dGhWQT09'")
#cmd6 = os.system("curl -X GET --header 'Accept: application/json' 'https://api.signupgenius.com/v2/k/user/profile/?user_key=V0FzMkxZcmVOZlVnclZMVEl6dGhWQT09'")
#cmd7 = os.system("curl -X GET --header 'Accept: application/json' 'https://api.signupgenius.com/v2/k/user/profile/?user_key=V0FzMkxZcmVOZlVnclZMVEl6dGhWQT09'")
#cmd8 = os.system("curl -X GET --header 'Accept: application/json' 'https://api.signupgenius.com/v2/k/user/profile/?user_key=V0FzMkxZcmVOZlVnclZMVEl6dGhWQT09'")
#cmd9 = os.system("curl -X GET --header 'Accept: application/json' 'https://api.signupgenius.com/v2/k/user/profile/?user_key=V0FzMkxZcmVOZlVnclZMVEl6dGhWQT09'")

pprint(cmd1)
'''


'''
	REFS:
		- https://projects.propublica.org/nonprofits/api
'''

organization = input("Please enter a charitable organization:	")
#print(organization)
print()

api_endpoint_org = "https://projects.propublica.org/nonprofits/api/v2/search.json?q={}".format(organization)
cmd10 = os.system("curl {}".format(api_endpoint_org))
pprint(cmd10)
