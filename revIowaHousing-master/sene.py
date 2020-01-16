# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 11:41:17 2020

@author: deward
"""

"""
Conducting Featuring Engineering on the following fretures:
    GarageQual - Garage quality
    GarageCond - Garage condition
    PavedDrive - Paved driveway
    PoolQC     - Pool quality

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def feature_extract(data: pd.DataFrame) -> pd.DataFrame:
    """
    I am doing Feature Engineering for the following features:
        GarageQual - Garage quality
        GarageCond - Garage condition
        PavedDrive - Paved driveway
        PoolQC     - Pool quality

    Parameters
    ----------
    data : pd.DataFrame
        This is the household dataframe we are working with.

    Returns
    -------
    DataFrame
        This function is going to return datafram.

    """

    # List of features:
    features = ['GarageQual', 'GarageCond', 'PoolQC','PavedDrive']
    features1 = ['GarageQual', 'GarageCond', 'PoolQC']
    features2 = 'PavedDrive'
    
    # Filter features from the dataframe:
    df = data[features]
    
    # Handling missing values:
        # There are no actual missing values, 'NA' are lables that represent 'Not available'
    
    # #####################################################
    # Convert categorical variables to numerical values:
    
    # a) Let's fill all the missing values with "NA" for consistency
    df_fillNa = df.fillna('NA')
    
    # b) Crete a list of the lables in our dataframe
    list1 = ['NA', 'Po','Fa', 'TA','Gd','Ex']
    list2 = ['N','P','Y']
    
    # Creating a range between 0 to 5 for the list1 and range between 0 to 3 for list2
    num1 = list(range(6))
    num2 = list(range(3))
    
    # Mapping numbers to our lists created above
    map1 = dict(zip(list1, num1))
    map2 = dict(zip(list2, num2))
    
    # Applying the function to the datafram columns:
    for col in features1:
        col2 = df_fillNa[col].apply(lambda x: map1[x])
        df_fillNa[col] = col2
    
    col3 = df_fillNa[features2].apply(lambda x: map2[x])
    df_fillNa[features2] = col3
    
    return df_fillNa
