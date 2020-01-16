#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 21:01:40 2020

@author: srwight
"""

__doc__ = """
Dependencies: pandas, numpy, scipy.stats

This module is for Feature Engineering on the following features:
    LowQualFinSF
    GrLivArea
    BsmtFullBath
    BsmtHalfBath
    FullBath
    
This is done in the function engineer(), which will receive the original
dataframe as input, treat any missing data and outliers, and adjust for
skew to help make the data fit a more normal distribution.

"""

import pandas as pd
import numpy as np
from scipy.stats import skew

def feature_extract(df:pd.DataFrame) -> pd.DataFrame:
    """
    Feature engineering for:
        LowQualFinSF
        GrLivArea
        BsmtFullBath
        BsmtHalfBath
        FullBath

    Parameters
    ----------
    df : pd.DataFrame
        This should be the entire Housing Prices dataframe.

    Returns
    -------
    pd.DataFrame
        This dataframe will include ONLY the engineered features
        listed above.
    """
    
    # Making a list of the features to be engineered to pass to various functions
    featurelist = ['LowQualFinSF',
                   'GrLivArea',
                   'BsmtFullBath',
                   'BsmtHalfBath',
                   'FullBath']
    
    curr_df = df[featurelist]
    
    # Handle Missing Values
    # -- There are none
    
    # Handle outliers by setting a max and min value that are 3 standard
    # deviations from the mean. Anything above or below those values will
    
    for column in featurelist:
        mean = curr_df[column].mean() # Calculate the mean for the column
        maxval = 3 * curr_df[column].std() + mean # mean + 3 stdev's
        minval = -3 * curr_df[column].std() + mean# mean - 3 stdev's
        
        #If the value is outside of the min and max, clip it to that value
        curr_df[column].clip(minval,maxval)
        
    # Handle skew
    # I decided to use log + 1 to bring the data closer to a normal
    # distribution.
        
    # set features_skew to a df that contains the skew values of the data    
    features_skew = curr_df.apply(skew)
    
    # Set the features_skew df to only contain skew values that are >0.75.
    # Arbitrary selection; we want normal-distribution data, so higher than
    # 0.75 would be counterproductive. 
    features_skew = features_skew[features_skew > 0.75]
    
    # use the index of features_skew to select which columns to log+1 transform
    logged_df = np.log(curr_df[features_skew.index]+1)
    curr_df = curr_df.drop(features_skew.index, axis=1)
    curr_df = pd.concat([curr_df, logged_df], axis=1 )
    
    return curr_df
    

# this section is entirely for testing purposes. When it is imported,
# it will not run.

def main():
    df=pd.read_csv('train.csv')
    print(feature_extract(df))
    
if __name__ == '__main__':
    main()
