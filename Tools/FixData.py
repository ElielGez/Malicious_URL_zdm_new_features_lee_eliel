import pandas as pd 

df = pd.read_csv('./base_pdns_ssl.csv')

sum=0
items=0
############ Fix dist geo locations ##############
dist_geo_location = df['distinct_geo_locations']

for index, element in enumerate(dist_geo_location):
    if element != -1:
        sum+= element
        items+=1
#print(f'sum: {sum}, items: {items} avg: {int(sum/items)}')
dist_avg= int(sum/items)
for index, element in enumerate(dist_geo_location):
    if element == -1:
        df['distinct_geo_locations'][index] = dist_avg

######## Fix AVG TTL ############
sum = 0
items = 0 
avg_ttl = df['avg_ttl']

for index, element in enumerate(avg_ttl):
    if element != 0:
        sum+=element
        items+=1
avg = sum/items
print(avg)
for index, element in enumerate(avg_ttl):
    if element == 0:
        df['avg_ttl'][index]=avg

########## FIX STD TTL ###############

sum = 0
items = 0 
avg_ttl = df['std_ttl']

for index, element in enumerate(avg_ttl):
    if element != 0 and pd.isnull(element) == False:
        sum+=element
        items+=1
avg = sum/items
print(avg)
for index, element in enumerate(avg_ttl):
    if element == 0 or pd.isnull(element) == True:
        df['std_ttl'][index]=avg

######## FIX Live Time ###########
sum = 0
items = 0 
life_time = df['life_time']

for index, element in enumerate(life_time):
    if element != -1 and element != 0:
        sum+=element
        items+=1
avg = sum/items
print(avg)
for index, element in enumerate(life_time):
    if element == -1 or element == 0:
        df['life_time'][index]=avg


######### FIX Active Time ###########
sum = 0
items = 0 
active_time = df['active_time']

for index, element in enumerate(active_time):
    if element != -1 and element != 0 :
        sum+=element
        items+=1
avg = sum/items
print(avg)
for index, element in enumerate(active_time):
    if element == -1 or element == 0:
        df['active_time'][index]=avg


########## FIX PDNS ###############
sum = 0
items = 0 
passive_dns = df['passive_dns']

for index, element in enumerate(passive_dns):
    if element != -1 and element != 0 :
        sum+=element
        items+=1
avg = int(sum/items)
print(avg)
for index, element in enumerate(passive_dns):
    if element == -1 or element == 0:
        df['passive_dns'][index]=avg

df.drop('Unnamed: 0', inplace=True, axis=1)

df.to_csv('fixed_base_pdns_ssl.csv')
