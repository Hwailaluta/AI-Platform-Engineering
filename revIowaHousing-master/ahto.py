#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ahtouw
"""
__doc__ = """
Dependencies: pandas
This module is for Feature Engineering on the following features:
    Utilities
    LotShape
    LandContour
    LotConfig
NOTE: These features are all categorical in nature

This is done in the function engineer(), which will receive the original
dataframe as input and one-hot encode essential features
"""
import pandas as pd

def feature_extract(df:pd.DataFrame) -> pd.DataFrame:
    """
    Feature engineering for:
        Utilities
        LotShape
        LandContour
        LotConfig
    Parameters
    ----------
    df : pd.DataFrame
        This should be the entire Housing Prices dataframe.
    Returns
    -------
    pd.DataFrame
        This dataframe will include ONLY the engineered features
        listed above.
        NOTE: 'Utilities' feature will be dropped
    """
    # Making a list of the features to be engineered to pass to various functions
    featureList = ['LotShape','LandContour','LotConfig','Utilities']
    feats_df = df[featureList]

    # No Missing Values or Outliers to handle

    # DROPPING THIS FEATURE - only 1 instance of different value, no significance
    feats_df = feats_df.drop('Utilities',axis=1)
    
    # The remaining feature list can all be one-hot encoded
    feats_df = pd.get_dummies(feats_df)
    return feats_df


def main():
    df=pd.read_csv('train.csv')
    new_df = feature_extract(df)
    print(new_df)
if __name__ == '__main__':
    main()

