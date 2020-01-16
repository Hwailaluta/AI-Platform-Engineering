'''
    @author: dhend
'''

import pandas as pd
def feature_extract(df):
    '''
    This addresses the following variables: exterior1st, exterior2nd, roofmatl, and masvnrtype.
    Exterior2nd is dropped. The continuous variables have skew applied.
    '''

    features = df[['Exterior1st', 'RoofMatl', 'MasVnrType']]

    #Dummy variables are given for categorical variables.
    ex1st = pd.get_dummies(df['Exterior1st'])
    roof = pd.get_dummies(df['RoofMatl'])
    mast = pd.get_dummies(df['MasVnrType'])

    #Exterior2nd was nearly identical to Exterior1st, so I dropped it.
    features = pd.concat([ex1st, roof, mast], axis=1)

    return features


def main():
    df=pd.read_csv('train.csv')
    print(feature_extract(df))
if __name__ == '__main__':
    main()
