import pandas as pd
from urllib.parse import urlparse

'''
Length of domains and number of consecutivecharacters
'''
def consecutive_characters(str):
    l = len(str)
    count = 0
    res = str[0]
    for i in range(l):   
        cur_count = 1
        for j in range(i + 1, l):
            if (str[i] != str[j]):
                break
            cur_count += 1
        if cur_count > count:
            count = cur_count
            res = str[i]
    return count


df= pd.read_csv('./CollectPDNS.csv')

domains= df['0']
results = []
con_chars = []
for index, domain in enumerate(domains):
    print(f'Run {index}/{len(domains)}')
    new_domain = urlparse(domain).netloc
    results.append(len(new_domain))
    con_chars.append(consecutive_characters(new_domain))

df['4']=results
df['5'] = con_chars
df.drop('Unnamed: 0', inplace=True, axis=1)
try:
    df.to_csv('./LengthOfDomains2.csv')
except:
    textfile = open("LengthOfDomains.txt", "w")
    for element in results:
        textfile.write(element + "\n")
    textfile.close()

    