import pandas as pd
from riskiq.api import Client
from urllib.parse import urlparse


API_SECRET="8c1cf1a737c204b9"
API_KEY="/XOX1muJq/3Wy9aKSQSutVFYFtl2XVTE"
client = Client(API_SECRET, API_KEY)

df= pd.read_csv('./collectTTL.csv')
domains= df['0']
errors=0
results=[]


#response=client.get_dns_data_by_name('google.com',rrtype=None, maxresults=10000)
#print(response['recordCount'])


for index, domain in enumerate(domains):
    print(f'Run {index}/{len(domains)}')
    new_domain = urlparse(domain).netloc
    try:
        response=client.get_dns_data_by_name(new_domain,rrtype=None, maxresults=1000)
        results.append(int(response['recordCount']))
    except:
        errors+=1
        print(f'Error number {errors}')
        results.append(-1)
    
    
df['3']=results
df.drop('Unnamed: 0', inplace=True, axis=1)
try:
    df.to_csv('./CollectPDNS2.csv')
except:
    textfile = open("CollectPDNS.txt", "w")
    for element in results:
        textfile.write(element + "\n")
    textfile.close()
