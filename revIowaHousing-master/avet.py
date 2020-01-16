# -*- coding: utf-8 -*-
"""
@author: avetisyang
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def feature_extract(data) -> pd.DataFrame:
    """
    Parameters
    ----------
    Returns Data Frane with 4 dependent variables:
	['MSSubClass','MSZoning', 'Street', 'Alley']

    """
	# I know about the conventions and ideally you are not supposed to import libraries inside the function, however, I
	# do remember that I brought this up during the class and the suggestions was made to go ahead and proceed with libraries 
	# being imported, since, it doesn't bother and conflit the code. just to be safe. 
    


    #data = pd.read_csv("train.csv")
    my_features = ['MSSubClass', 'MSZoning', 'Street', 'Alley']
    data = data[my_features]

    # dataframe with categorical features
    categorical_columns = [col for col in data.columns if data[col].dtype == 'object']
    data_cat = data[categorical_columns]

    # dataframe with numerical features
    data_num = data.drop(categorical_columns, axis=1)

    from scipy.stats import skew

    data_num_skew = data_num.apply(lambda x: skew(x.dropna()))
    data_num_skew = data_num_skew[data_num_skew > .75]

    # apply log + 1 transformation for all numeric features with skewnes over .75
    data_num[data_num_skew.index] = np.log1p(data_num[data_num_skew.index])

    # Printing total numbers and percentage of missing data
    # total = data.isnull().sum().sort_values(ascending=False)
    # percent = (data.isnull().sum() / data.isnull().count()).sort_values(ascending=False)
    # missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])

    # The column 'Alley' has more than 90% missing values so we delet the whole column!!!
    # We may leave the data as it is or do data imputation
    # to replace them. Suppose the number of cases of missing values is extremely small;
    # then we may drop or omit those values from the analysis. In statistical language,
    # if the number of the cases is less than 5% of the sample, then we can drop them.
    # If there is a larger number of missing values, then it is
    # better to drop those cases (rather than do imputation) and replace them.

    # checks what is the percentage of missing values in categorical dataframe
    for col in data_num.columns.values:
        missing_values = data_num[col].isnull().sum()
        # print("{} - missing values: {} ({:0.2f}%)".format(col, missing_values, missing_values/data_len*100))

        # drop column if there is more than 50 missing values
        if missing_values > 260:
            # print("droping column: {}".format(col))
            data_num = data_num.drop(col, axis=1)
        # if there is less than 260 missing values than fill in with median valu of column
        else:
            # print("filling missing values with median in column: {}".format(col))
            data_num = data_num.fillna(data_num[col].median())
    # so we exclude 'Alley' from our analysis


    # TURNING CATEGORICAL VARIABLES INTO DUMMY VARIEBLES SO COMPUTER CAN EASILY UNDERSTAND WHATS HAPENNING
    # Using pandas.get_dummies function to Convert categorical variable into dummy/indicator variables
    data_cat_dummies = pd.get_dummies(data_cat, drop_first=True)
    # Printing number of categorical variables including dummy variables
    # print("Categorical variables : " + str(len(data_cat_dummies.columns)))
    return data_cat_dummies

