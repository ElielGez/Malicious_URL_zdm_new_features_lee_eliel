import pandas as pd
from riskiq.api import Client
from urllib.parse import urlparse
import requests
import base64
import json


API_SECRET="8c1cf1a737c204b9"
API_KEY="/XOX1muJq/3Wy9aKSQSutVFYFtl2XVTE"
client = Client(API_SECRET, API_KEY)

df= pd.read_csv('./LengthOfDomains.csv')
domains= df['0']
errors=0
results=[]

url_to_scan = ''
      
url = f'https://api.riskiq.net/v1/ssl/cert/host?host={url_to_scan}'
headers = {'Accept': 'application/json','Authorization': 'Basic OGMxY2YxYTczN2MyMDRiOTovWE9YMW11SnEvM1d5OWFLU1FTdXRWRllGdGwyWFZURQ=='}

for index, domain in enumerate(domains):
    new_domain = urlparse(domain).netloc
    print(f'Run {index}/{len(domains)}')
    url = f'https://api.riskiq.net/v1/ssl/cert/host?host={new_domain}'
    res = requests.get(url, headers=headers)
    data =json.loads(res.text)
    content = data['content']
    final=0
    if content != [] :
        first_seen= int(content[0]['firstSeen'])
        last_seen = int (content[0]['lastSeen'])
        final=last_seen-first_seen
    results.append(final)

df['6']=results
df.drop('Unnamed: 0', inplace=True, axis=1)
try:
    df.to_csv('./CollectSSL.csv')
except:
    textfile = open("CollectSSL.txt", "w")
    for element in results:
        textfile.write(element + "\n")
    textfile.close()
