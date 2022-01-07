import pandas as pd
from collections import defaultdict
from urllib.parse import urlparse
import math


df = pd.read_csv('Final_newData_withFeatures.csv')

urls = df['0']

entropies = []

for index, url in enumerate(urls):
    domain=""
    if url[:4] == 'http':
        domain  = urlparse(url).netloc
    else:
        domain = urlparse('http://'+url).netloc
    
    entropy  = 0
    str_len  = len(domain)
    chars    = defaultdict(int)
    for char in domain:
        chars[char] += 1
    for char in domain:
        pj       = (chars[char]/str_len)
        entropy  += pj*math.log(pj,2)
    entropies.append((-1)*entropy)

df['6'] = pd.Series(entropies)

#df.drop('Unnamed: 0', inplace=True, axis=1)
#df=df[df['length'] != -1]
df.to_csv('superFinal.csv')