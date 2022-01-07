import requests, os, json, time
import pandas as pd
import re
import concurrent.futures

domains_file = './CheckActive.csv'
df           = pd.read_csv(domains_file) 

domains= df['0']
is_active=df['11']
is_malicious=df['10']
new_data=[]
for index, domain in enumerate(domains):
    if is_active[index] != "Not-Active":
        new_data.append([domain,is_malicious[index]])

new_df = pd.DataFrame(new_data, columns=['0', '1'])
new_df.to_csv('ActiveDomains.csv')

def statistics(csv_path):
    import pandas as pd
    df = pd.read_csv(csv_path)
    total = 0
    malicous = 0
    for index, row in df.iterrows():
        total = total + 1
        if(row['1'] == 1):
            malicous = malicous + 1
    print("Malicous: "+str((malicous/total)*100))

statistics("./ActiveDomains.csv")

# Storing all builtwith data of given url csv file (domain_file) to files in a folder
domains_file = './NewMaliciousDomains.csv'
df           = pd.read_csv(domains_file)

domains= df['0']
df['2']=""
counter=0
for index, domain in enumerate(domains):
    print(f'Run number {index}/{len(domains)}')
    url = f'https://api.builtwith.com/free1/api.json?KEY=b3051c45-25c1-4ac5-b13a-c840091d0841&LOOKUP={domain}'
    res = requests.get(url)
    ans = res.text
    if ans.find('Errors') != -1:
        print(ans)
        time.sleep(1)
        res = requests.get(url)
        ans = res.text
        if ans.find('Errors') != -1:
            df['2'][index]="-1"
            counter+=1
            print(f'Error Number {counter}')
        
    filename=f'{index}.txt'
    savepath='C:\\Users\\Zohar_ysncvfn\\Desktop\\newMalBuiltwith'
    fullname=os.path.join(savepath, filename)
    print(fullname)
    file1 = open(fullname, "w")
    file1.write(ans)
    file1.close()
    time.sleep(0.4)
        
    

#Sorting all files to check which domains has no response from builtwith api (1564 in total)
#marking in -1 in the new csv file 

path = 'C:\\Users\\XXXX\\Desktop\\BuiltwithData'#Replace with your desired path
bad_domains=[]
files = os.listdir(path)
counter=0
for f in files:
    fullpath= path+ '\\' + f
    file = open(fullpath, "r")
    data=file.read()
    if data.find('Errors')!=-1:
        bd= f[:-4]
        bad_domains.append(bd)

domains_file = './ActiveDomains.csv'
df           = pd.read_csv(domains_file)
df['2']=""
print(bad_domains)
for bd in bad_domains:
    df['2'][int(bd)]="-1"

df.drop('Unnamed: 0', inplace=True, axis=1)
df.to_csv('UpdatedActiveDomains.csv')        
	
'''

'''
#extracting length of each api response length

domains_file='./NewMaliciousDomains.csv'
df= pd.read_csv(domains_file)
#is_active= df['2']
df['length']=""
path = 'C:\\Users\\XXXX\\Desktop\\newMalBuiltwith' #Replace with your desired path
files = os.listdir(path)

for f in files:
    domain_index=int(f[:-4])
    fullpath= path+ '\\' + f
    file = open(fullpath, "r")
    data=file.read()
    df['length'][domain_index]=len(data)
    


df.drop('Unnamed: 0', inplace=True, axis=1)
df.to_csv('newMalLength.csv')

#AVG of builtwith length data

domains_file='./superFinal.csv'
df=pd.read_csv(domains_file)
benign_sum=0
benign_quantity=0
malicious_sum=0
malicious_quantity=0

for index, row in df.iterrows():
    if row['2'] !=-1:
        if row['1'] == 1:
            malicious_quantity+=1
            malicious_sum+=row['2']
        elif row['1'] == 0:
            benign_quantity+=1
            benign_sum+=row['2']
mal_avg=(malicious_sum/malicious_quantity)
benign_avg=(benign_sum/benign_quantity)
print(f'Malicious AVG length: {mal_avg}')
print(f'Benign AVG length: {benign_avg}')

# creates analytics feature

domains_file='./newMalLength.csv'
df=pd.read_csv(domains_file)
path = 'C:\\Users\\Zohar_ysncvfn\\Desktop\\newMalBuiltwith'
files = os.listdir(path)
df['analytics']=""
for f in files:
    domain= f[:-4]
    print(domain)
    fullpath= path+ '\\' + f
    file = open(fullpath, "r")
    data=file.read()
    file.close()
    if data.find('analytics","live"')!=-1:
        
        index=data.find('analytics","live"')
        temp_data=data[index:]
        end_index=temp_data.find('"latest"')
        new_data=temp_data[:end_index]
        a = re.split(',|:',new_data)
        analytics_number=int(a[2])+int(a[4])
        df['analytics'][int(domain)]=analytics_number
    else:
        df['analytics'][int(domain)]=0

df.drop('Unnamed: 0', inplace=True, axis=1)
df.to_csv('newMalAnalytics.csv')

#AVG of builtwith analytics data           

domains_file='./superFinal.csv'
df=pd.read_csv(domains_file)
benign_sum=0
benign_quantity=0
malicious_sum=0
malicious_quantity=0

for index, row in df.iterrows():
    if row['3'] !=-1:
        if row['1'] == 1:
            malicious_quantity+=1
            malicious_sum+=row['3']
        elif row['1'] == 0:
            benign_quantity+=1
            benign_sum+=row['3']
            #print(benign_sum, index)
mal_avg=(malicious_sum/malicious_quantity)
benign_avg=(benign_sum/benign_quantity)
print(f'Malicious AVG analytics: {mal_avg}')
print(f'Benign AVG analytics: {benign_avg}')

#Union of newMal and base data

new_mal_df      = pd.read_csv('./newMalAnalytics.csv')
base_data_df    = pd.read_csv('./DomainsBuiltwithAnalytics.csv')
base_domains= base_data_df['0']
end_newMal_index= 7117


for index, domain in enumerate(base_domains):
    if base_data_df['1'][index] == 0:
        #print(domain, base_data_df['3'][index],base_data_df['4'][index] )
        print(index)
        df2 = pd.DataFrame([[domain, "0",str(base_data_df['3'][index]), str(base_data_df['4'][index]) ]],\
             columns=['0','1','length','analytics'])
        
        new_mal_df=new_mal_df.append(df2, ignore_index=True)
    

new_mal_df.drop('Unnamed: 0', inplace=True, axis=1)
new_mal_df.to_csv('./NewDataUnion.csv')
