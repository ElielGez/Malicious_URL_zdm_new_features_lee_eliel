import pandas as pd 

new_mal         = pd.read_csv('./fixed_base_pdns_ssl.csv')
base_all        = pd.read_csv('./base_(all).csv')
final_pd        = pd.read_csv('./NewDataUnion.csv')
old_features    = pd.read_csv('./old_features.csv')

dom_length              = []
consecutive_chars       = []
entropy                 = []
num_of_ips              = []
distinct_geo_locations  = []
avg_ttl                 = []
std_ttl                 = []
life_time               = []
active_time             = []
passive_dns             = []
ssl_time                = []
car                     = []
ccr                     = []

base_domains = base_all['0']


## Map between the indexes of the lists ###
match_dict = dict()
new_domains = new_mal['url']
for index, domain in enumerate(new_domains):
    match_dict[domain]=index

## Add feature of new malicious domains ## 
mal_final_domains = []
for index, row in final_pd.iterrows():
    if row['1'] == 1:
        mal_final_domains.append(row['0'])

for index, domain in enumerate(mal_final_domains):
    if domain in match_dict:
        old_index = match_dict[domain]
        dom_length.append(new_mal['dom_length'][old_index])
        consecutive_chars.append(new_mal['consecutive_chars'][old_index])
        entropy.append(new_mal['entropy'][old_index])
        num_of_ips.append(new_mal['num_of_ips'][old_index])
        distinct_geo_locations.append(new_mal['distinct_geo_locations'][old_index])
        avg_ttl.append(new_mal['avg_ttl'][old_index])
        std_ttl.append(new_mal['std_ttl'][old_index])
        life_time.append(int(int(new_mal['life_time'][old_index])/31536000))
        active_time.append(int(int(new_mal['active_time'][old_index])/31536000))
        passive_dns.append(new_mal['passive_dns'][old_index])
        ssl_time.append(new_mal['ssl_time'][old_index])
        ccr.append(new_mal['ccr'][old_index])
        car.append(new_mal['car'][old_index])
        
    else:
        dom_length.append(-1)
        consecutive_chars.append(-1)
        entropy.append(-1)
        num_of_ips.append(-1)
        distinct_geo_locations.append(-1)
        avg_ttl.append(-1)
        std_ttl.append(-1)
        life_time.append(-1)
        active_time.append(-1)
        passive_dns.append(-1)
        ssl_time.append(-1)
        ccr.append(-1)
        car.append(-1)


## Map between the indexes of the lists ###
benign_index = dict()
for index, row in old_features.iterrows():
    if row['17'] == 0:
        benign_index[row['0']] = index

## Add features of benign domains ## 
ben_final_domains = []
for index, row in final_pd.iterrows():
    if row['1'] == 0:
        ben_final_domains.append(row['0'])

for index, domain in enumerate(ben_final_domains):
    if domain in benign_index:
        old_index = benign_index[domain]
        dom_length.append(old_features['1'][old_index])
        consecutive_chars.append(old_features['2'][old_index])
        entropy.append(old_features['3'][old_index])
        num_of_ips.append(old_features['4'][old_index])
        distinct_geo_locations.append(old_features['5'][old_index])
        avg_ttl.append(old_features['6'][old_index])
        std_ttl.append(old_features['7'][old_index])
        life_time.append(old_features['8'][old_index])
        active_time.append(old_features['9'][old_index])
        passive_dns.append(old_features['13'][old_index])
        ssl_time.append(old_features['15'][old_index])
        ccr.append(old_features['10'][old_index])
        car.append(old_features['11'][old_index])
        
    else:
        dom_length.append(-1)
        consecutive_chars.append(-1)
        entropy.append(-1)
        num_of_ips.append(-1)
        distinct_geo_locations.append(-1)
        avg_ttl.append(-1)
        std_ttl.append(-1)
        life_time.append(-1)
        active_time.append(-1)
        passive_dns.append(-1)
        ssl_time.append(-1)
        ccr.append(-1)
        car.append(-1)


final_pd['dom_length']= pd.Series(dom_length)
final_pd['consecutive_chars']=pd.Series(consecutive_chars)
final_pd['entropy']=pd.Series(entropy)
final_pd['num_of_ips']=pd.Series(num_of_ips)
final_pd['distinct_geo_locations']=pd.Series(distinct_geo_locations)
final_pd['avg_ttl']=pd.Series(avg_ttl)
final_pd['std_ttl']=pd.Series(std_ttl)
final_pd['life_time']=pd.Series(life_time)
final_pd['active_time']=pd.Series(active_time)
final_pd['passive_dns']=pd.Series(passive_dns)
final_pd['ssl_time']=pd.Series(ssl_time)
final_pd['ccr']=pd.Series(ccr)
final_pd['car']=pd.Series(car)

final_pd.drop('Unnamed: 0', inplace=True, axis=1)
res=None

final_pd=final_pd[final_pd['dom_length'] != -1]
'''
for index, row in final_pd.iterrows():
    print(f'Run {index}')
    if row['dom_length'] == -1:
        final_pd=final_pd.drop(index, axis=0)
'''
final_pd.to_csv('./Final_newData_withFeatures.csv')




    
        
