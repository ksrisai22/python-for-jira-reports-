import requests
import json
from requests.auth import HTTPBasicAuth
from pprint import pprint 

#getting issue details

r= requests.get('https://srisai.atlassian.net/rest/api/2/issue/FB-10', auth=HTTPBasicAuth('f20140693@goa.bits-pilani.ac.in', 'kgb156@$'))
#r= requests.get('https://srisai.atlassian.net/rest/api/2/issue/', auth=HTTPBasicAuth('f20140693@goa.bits-pilani.ac.in', 'kgb156@$'))
#get IDs for getting sprint details
'''
r= requests.get('https://srisai.atlassian.net/rest/greenhopper/1.0/rapidview', auth=HTTPBasicAuth('f20140693@goa.bits-pilani.ac.in', 'kgb156@$'))
'''
q = requests.get('https://srisai.atlassian.net/rest/greenhopper/1.0/sprints/7', auth=HTTPBasicAuth('f20140693@goa.bits-pilani.ac.in', 'kgb156@$'))
t = requests.get('https://srisai.atlassian.net/rest/greenhopper/1.0/rapid/charts/sprintreport?rapidViewId=6&sprintId=1', auth=HTTPBasicAuth('f20140693@goa.bits-pilani.ac.in', 'kgb156@$'))
#converting request object to dictionary

p1 = t.json()    
s1 = json.dumps(p1)
p2 = json.loads(s1)

pprint(p2)

##printing all the json
#pprint(p2['fields']['status']['name'])
#aceesing nested dictionary to get requoired keys
'''
li = p2['fields']['comment']['comments']
dic = li[0]
print(dic['body'])


for k,v in p2.items():
    print('{} : {}'.format(k,v))s
'''

