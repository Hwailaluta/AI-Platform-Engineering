# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 14:05:31 2020

@author: paisl
"""

import pandas as pd


def feature_extract(df:pd.DataFrame) -> pd.DataFrame:
    
    '''
    Feature engineering for:
        Electrical
        Heating
        HeatingQC
        KitchenQual
        CentralAir
    '''
    # Isolate my features
    featurelist = ['Electrical',
                   'Heating',
                   'HeatingQC',
                   'KitchenQual',
                   'CentralAir']
    
    curr_df = df[featurelist]
    
    #Fill 1 missing Electrical value with the mode 
    mode = 'SBrkr'
    curr_df.Electrical = curr_df.Electrical.fillna(mode)
    
    #Generate dummy columns
    curr_df = pd.get_dummies(curr_df, columns=['Electrical','Heating','HeatingQC','KitchenQual','CentralAir'],drop_first=True)
    
    return curr_df

