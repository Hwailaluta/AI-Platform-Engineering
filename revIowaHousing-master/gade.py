# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 12:32:12 2020

@author: rooga
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def feature_extract(data:pd.DataFrame):
    #getting my feautres into a seprate data frame
    my_features = data[['BsmtQual','ExterQual','ExterCond','Foundation']]
    #creating a list of my features 
    listoffeatures=['BsmtQual','ExterQual','ExterCond']
    #checking if there is any missing value and fill it in with 0
    my_features = my_features.fillna('NA')
    #creating a list of the the ratings 
    myvars = ['NA','Po', 'Fa', 'TA', 'Gd', 'Ex']
    # Then we make a list of values from 0 to 5 that we want to apply to our ratings
    myvals = list(range(6))
    #creating a dictionary to map values to ratings 
    mymap = dict(zip(myvars, myvals))
    #creating a loop in my features list to check what rate and pass a value in a new list
    for column in listoffeatures:
        newcol = my_features[column].apply(lambda x: mymap[x])
        #drop the old list 
        my_features.drop(column, axis=1, inplace=True)
        #assign the new list to my old list 
        my_features[column]=newcol
    #getting my dummy features     
    my_dummy_features = pd.get_dummies(my_features)
    #concate all my features (the dummy and my_features) to one data frame 
    my_features = pd.concat([my_features,my_dummy_features],axis = 1)
    #return the data frame 
    return my_features 
