# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 15:50:14 2020

@author: eende
"""

import pandas as pd

__doc__ = """

Dependencies: pandas

This module is for feature engineering on the following features:
    BsmtCond
    BsmtExposure
    BsmtFinType1
    BsmtFinType2
    
This module converts the defined features from Objects to Strings so that they can be used
as categorical data.  It then creates a new DataFrame named basement_data and inserts
the new categorical features into it.  

"""

def feature_extract(df: pd.DataFrame) -> pd.DataFrame :
    
    """
    
    Parameters:
        df: pd.DataFrame = The entire Housing Prices DataFrame
        
    Returns:
        pd.DataFrame = known as basement_data, returns numbered gradients of
        previously String values in each column
        
    """
    
    # Fills nan values with NA in each column
    df['BsmtCond'] = df['BsmtCond'].fillna('NA')
    df['BsmtExposure'] = df['BsmtExposure'].fillna('NA')
    df['BsmtFinType1'] = df['BsmtFinType1'].fillna('NA')
    df['BsmtFinType2'] = df['BsmtFinType2'].fillna('NA')
    
    # Converting feature objects into strings
    df['BsmtCond'] = df['BsmtCond'].astype(str)
    df['BsmtExposure'] = df['BsmtExposure'].astype(str)
    df['BsmtFinType1'] = df['BsmtFinType1'].astype(str)
    df['BsmtFinType2'] = df['BsmtFinType2'].astype(str)
    
    
    
    condvars = ['NA','Po', 'Fa', 'TA', 'Gd', 'Ex'] # Map variables for BsmtCond
    expvars = ['NA', 'No', 'Mn', 'Av', 'Gd'] # Map variables for BsmtExposure
    finvars = ['NA', 'Unf', 'LwQ', 'Rec', 'BLQ', 'ALQ', 'GLQ'] # Map variables for BsmtFinType

    condvals = list(range(6)) # List of values for BsmtCond
    expvals = list(range(5)) # List of values for BsmtExp
    finvals = list(range(7)) # List of values for BsmtFinType
    
    condmap = dict(zip(condvars, condvals)) # Map for BsmtCond
    expmap = dict(zip(expvars, expvals)) # Map for BsmtExposure
    finmap = dict(zip(finvars, finvals)) # Map for BsmtFinType

    # Maps numbers 0 - 5 to values NA, Po, Fa, Ta, Gd, Ex respectively
    newcol = df['BsmtCond'].apply(lambda x: condmap[x])
    df['BsmtCond'] = newcol
    
    # Maps numbers 0 - 4 to values NA, No, Mn, Av, Gd respectively
    newcol = df['BsmtExposure'].apply(lambda x: expmap[x])
    df['BsmtExposure'] = newcol
    
    # Both FinType maps map numbers 0 - 6 to values NA, Unf, LwQ, Rec, BLQ, ALQ, GLQ respectively
    newcol = df['BsmtFinType1'].apply(lambda x: finmap[x])
    df['BsmtFinType1'] = newcol
    
    newcol = df['BsmtFinType2'].apply(lambda x: finmap[x])
    df['BsmtFinType2'] = newcol
    
    
    basement_data = pd.DataFrame()
    myFeatures = ['BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2']
    
    # Inserting String features into basement_data DataFrame
    for feature in myFeatures:
        basement_data.insert(loc=0,column=feature,value=df[feature])
    
    return basement_data
   

# This section for testing purposes only
def main():
    data = pd.read_csv(r"C:\Users\eende\Desktop\House Price Dataset\train.csv")
    print(feature_extract(data))
    
if __name__ == '__main__':
    main()
