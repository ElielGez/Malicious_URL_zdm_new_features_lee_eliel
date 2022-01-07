import requests, os, json, time
import pandas as pd
""" TODO: 
    add features to df: eg. javascripts, widgets, language, frameworks, analytics

"""

#domains_file = '../Datasets/features_extractions/base_(all).csv'
domains_file = './new_mal_urls.csv'

#path               = os.path.dirname(os.path.abspath(__file__))

#df = pd.read_csv(path+'/'+domains_file) 
df= pd.read_csv(domains_file)
domains = df['url']
df['builtwith']=""
print(domains)
counter=0
url=""
error_counter=0
for index, domain in enumerate(domains):
    print(f'Run number {index} / {len(domains)}')
    if counter%3 == 0:
        url = f'https://api.builtwith.com/free1/api.json?KEY=b3051c45-25c1-4ac5-b13a-c840091d0841&LOOKUP={domain}'
    elif counter%3 == 1:
        url= f'https://api.builtwith.com/free1/api.json?KEY=1a30a8d5-3080-4792-8c0e-730c89436e83&LOOKUP={domain}'
    elif counter%3 == 2:
        url=f'https://api.builtwith.com/free1/api.json?KEY=c72cbb9a-039b-4e5d-8848-fa90af9b0168&LOOKUP={domain}'

   
    res = requests.get(url)
    ans = res.text
    time.sleep(0.4)
    if ans.find('Errors') != -1:
        error_counter+=1
        print(ans)
        df['builtwith'][index]="-1"
        
        print(f'Error number {error_counter}')

    counter+=1
new_df=df[['url', 'builtwith']].copy()
new_df.to_csv('CheckedBuiltwith.csv')

df = pd.read_csv('CheckedBuiltwith.csv')
domains = df['url']
new_domains=[]
for index, domain in enumerate(domains):
    if df['builtwith'][index]!= -1:
        new_domains.append([domain,"1"])

new_df = pd.DataFrame(new_domains, columns=['0', '1'])
new_df.to_csv('NewMaliciousDomains.csv')

        
    
