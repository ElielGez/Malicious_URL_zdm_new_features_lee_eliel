import pandas as pd
import numpy as np
import ast
import time
import math
from ast import literal_eval
import os
##Communication Countries rating
def CCR(countries):
    CCR_NAME = 'countries_(75-25).csv'
    countries_ratios = pd.read_csv(CCR_NAME, sep=';')
    countries_ratios["total_normalize"] = (countries_ratios["total"] - countries_ratios["total"].min()) / (
            countries_ratios["total"].max() - countries_ratios["total"].min())
    countries_threshold = 9
    rating = 0
    neg = 0.00001
    for country in countries:
        prec = 0.75
        calc = 1
        cur = countries_ratios[countries_ratios["code"]==country]
        if cur.shape[0]>0:
            country_total = int(cur["total"].iloc[0])
            if country_total>=countries_threshold:
                calc = float(cur["total_normalize"])+neg
                prec = float(cur["benign_ratio"])
                # rating+=math.log(prec+0.00001,0.5)
        # else:
        # 	print(country)
        rating+=math.log((prec)+neg,0.5)/calc
        # print("Prec %.5f, Calc %.9f, Total %.5f, Rating %.5f" % (prec, calc, math.log((prec)+neg,0.05)/(calc+neg), rating))
    return rating

## Communication ASNs Rank
def CAR (asns):
    CAR_NAME = 'asns_(75-25).csv'
    asns_ratios = pd.read_csv(CAR_NAME, sep=';')
    asns_ratios["total_normalize"] = (asns_ratios["total"] - asns_ratios["total"].min()) / (
            asns_ratios["total"].max() - asns_ratios["total"].min())
    asns_threshold = 2
    rating = 0
    neg = 0.00001
    for asn in asns:
        prec = 0.75
        calc = 1
        cur = asns_ratios[asns_ratios["code"]==asn]
        if cur.shape[0]>0:
            asn_total = int(cur["total"].iloc[0])
            if asn_total>=asns_threshold:
                calc = float(cur["total_normalize"])+neg
                prec = float(cur["benign_ratio"])
        rating+=math.log((prec)+neg,0.5)/calc
    return rating


if __name__ == '__main__':
    start = time.time()
    df = pd.read_csv('malicious.csv')
    country_codes = df['4']
    ccr_res = []
    '''
    for countries in country_codes:
        if pd.isnull(countries) == False:
            #print(countries, end='\t')
            lst = ast.literal_eval(countries)
            ccr_res.append(CCR(lst))
        else:
            ccr_res.append(-1)
    print('CCR feature created')
    '''
    car_res = []
    asns_codes = df['3']
    for asns in asns_codes:
        if (asns is not np.nan):
            lst = ast.literal_eval(asns)
            #print(CCR(lst))
            car_res.append(CAR(lst))
        else:
            ccr_res.append(-1)
    print('CAR feature created')
    #df['10'] = ccr_res
    #df['11'] = car_res
    new_df = pd.DataFrame()
    new_df['1']= car_res
    #new_df['2']= car_res
    #print(f'ccr length {len(ccr_res)} car length {len(car_res)}')
    new_df.to_csv('CCR_CAR.csv', index=False)
    end = time.time()
    print('File saved.')
    print('Time:\t'+str(end-start))
