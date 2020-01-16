# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 00:16:52 2020

@author: gmnya
"""

__doc__ = """
Dependencies: pandas, numpy, scipy.stats

This module is for Feature Engineering on the following 
features:
    BsmtUnfSF
    TotalBsmtSF
    1stFlrSF
    2ndFlrSF

This is done in the following function feature_extract(), which will
receive the original dataframe, and treat any missing data and 
outliers, and adjust for skewness to help make the data fit a 
normal distribution.

"""


import pandas as pd
import numpy as np
from scipy.stats import skew

def feature_extract(df:pd.DataFrame) -> pd.DataFrame:
    """
    Feature engineering for:
        BsmtUnfSF
        TotalBsmtSF
        1stFlrSF
        2ndFlrSF

    Parameters
    ----------
    df : pd.DataFrame
        This dataframe will only include ONLY the 
        above listed engineered features.

    Returns
    -------
    Complete dataframe with engineered features.

    """
    featurelist = ['BsmtUnfSF',
                   'TotalBsmtSF',
                   '1stFlrSF',
                   '2ndFlrSF']
    
    curr_df = df[featurelist]
    
    # Handle Missing Values
    # -- No missing values
    
    # Handle outliers by setting a Max and 
    # Min value that at 3 st. devs. from mean
    
    for column in featurelist:
        mean = curr_df[column].mean()
        maxval = mean + (3 * curr_df[column].std())
        minval = mean - (3 * curr_df[column].std())
        
        # If the vaalue is outside the minval and
        # maxval, clip it.
        curr_df[column].clip(minval,maxval)
        
    # Handle skew
    # I will use log + 1 to bring data closer to a
    # normal distribution
    
    # set feature_skew to a df that contains the
    # skew values of the data
    
    feature_skew = curr_df.apply(skew)
    
    # set feature_skew to only contain skew 
    # values over .75
    
    feature_skew = feature_skew[feature_skew > 0.75]
    
    # use the index of features_skew to select which
    # columns to log+1 transform
    
    logged_df = np.log(curr_df[feature_skew.index]+1)
    curr_df = curr_df.drop(feature_skew.index, axis=1)
    curr_df = pd.concat([curr_df, logged_df], axis=1 )
    
    return curr_df

# this section is entirely for testing purposes. When 
# it is imported, it will not run.

def main():
    df=pd.read_csv('train.csv')
    print(feature_extract(df))
if __name__ == '__main__':
    main()
