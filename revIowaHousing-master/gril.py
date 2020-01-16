#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 08:49:51 2020

@author: michael
"""

# Importing packages
import pandas as pd
import numpy as np
from datetime import datetime


#traindata = pd.read_csv("/home/michael/Downloads/Dataset(1)/train.csv")
#testdata = pd.read_csv("/home/michael/Downloads/Dataset(1)/test.csv")


def feature_extract(traindata):
    #Now we focus on my variables of interest
    mycolnames = ['MoSold','YrSold','YearBuilt','YearRemodAdd','GarageYrBlt']
    mydata = traindata[mycolnames]

    #GarageYrBlt has total missing values of 81 and percentage of missing values of  0.055479
    #we need to replace NaN values with the mean, 1978, since it results in the least standard deviation
    newcol = mydata['GarageYrBlt'].fillna(1978).apply(int)
    mydata['GarageYrBlt'] = newcol

    #this gives me a std deviation of 23.994863
    #I filled in NaN values with the mean, 1978
    
    
    # Need to use Dummy variables since my data points are in months('MoSold')
    df_temp = pd.get_dummies(data=mydata.MoSold,
                           prefix='MoSold',
                           prefix_sep= '_',
                           dummy_na=False)

    mydata.drop('MoSold', axis=1, inplace=True)

    # s: now we need to concatenate our dummies to our data

    retdata = pd.concat([mydata, df_temp], axis=1)
    return retdata

def main():
    df = pd.read_csv('train.csv')
    print(feature_extract(df))

if __name__ == '__main__':
    main()
