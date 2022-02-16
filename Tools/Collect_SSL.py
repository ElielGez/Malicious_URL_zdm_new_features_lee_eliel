import pandas as pd
from riskiq.api import Client
from urllib.parse import urlparse
import requests
import base64
import json
from datetime import datetime


API_SECRET="8c1cf1a737c204b9"
API_KEY="/XOX1muJq/3Wy9aKSQSutVFYFtl2XVTE"

client = Client(API_SECRET, API_KEY)

df= pd.read_csv('./newMalWithAds.csv')
domains= df['domain']
errors=0
results=[]

url_to_scan = ''
      
url = f'https://api.riskiq.net/pt/v2/ssl-certificate/history?query={url_to_scan}'
headers = {'Accept': 'application/json','Authorization': 'Basic bGVla29jaGF2QGdtYWlsLmNvbToxNmE3Mzc1NmI1MzRmNGNkZmY4ZDc5NzYwZTIxMzYxYjNkZTQ3ZTJiMGQxOGMyMWZhNmVhMjRlMTFkMWM5MThl'}

for index, domain in enumerate(domains):
    #new_domain = urlparse(domain).netloc
    new_domain = domain
    print(f'Run {index}/{len(domains)}')
    url = f'https://api.riskiq.net/pt/v2/ssl-certificate/history?query={new_domain}'
    res = requests.get(url, headers=headers)
    data =json.loads(res.text)
    content = data['results']
    final=0
    if content != [] :
        first_seen= int(datetime.fromisoformat(content[0]['firstSeen']).timestamp())
        last_seen = int (datetime.fromisoformat(content[0]['lastSeen']).timestamp())
        final=last_seen-first_seen
    results.append(final)

#ssl_time
df['ssl_time']=results
df.drop('Unnamed: 0', inplace=True, axis=1)
try:
    df.to_csv('./newMalWithAds.csv')
except:
    textfile = open("CollectSSL.txt", "w")
    for element in results:
        textfile.write(element + "\n")
    textfile.close()
