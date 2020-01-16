#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:57:22 2020

@author: staxx
"""
import pandas as pd

def feature_extract(df_train):
    '''
    

    Take in dataframe object 
    ----------
    df_train : dataframe
        training dataset from the Ames,Iowa housing file.

    Returns concatenated dataframe 
    -------
    dataframe object of extracted data and transformed variable.

    Looked for missing values and outliers and did not find any.
    
    
    '''
# create list of my respective values for evaluating 
    predictor_columns = ['Neighborhood','Condition1','Condition2']

# create dummy list of relevant values for evaluation
    df_housing = pd.get_dummies(df_train[predictor_columns])

# based off EDA LandSLope can be changed to numerical based of th three types
    df_train.LandSlope.replace({'Sev':1, 'Mod':2, 'Gtl':3}, inplace=True)
    
    return pd.concat([df_housing, df_train.LandSlope], axis=1)

