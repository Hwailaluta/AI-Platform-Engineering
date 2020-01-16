# Features: LotFrontage, LotArea, MasVnrArea, BsmtFinSF1, BsmtFinSF2

# Importing packages
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
from scipy.stats import skew
    

def feature_extract(dataframe):    
    
    # Create my dataframe
    myFeatures = ['LotFrontage', 'LotArea', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2', 'SalePrice']
    myDF = dataframe[myFeatures] # insert my features from the master dataframe into my dataframe
    
    # Separate out the target variable, SalePrice
    target = myDF['SalePrice'] # A Series containing the SalePrice data
    
    # Log transform the target variable
    target_log = np.log(target)
    
    # Drop target variable from dataset
    features_df = myDF.drop(["SalePrice"], axis=1)
    
    # Reduce skewness
    # Histograms to visualize skewness
    # myX.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8); 
    # Identify features with skew > .75 and apply log + 1 transformation
    data_skew = features_df.apply(lambda x: skew(x.fillna(x.median())))
    data_skew = data_skew[data_skew > .75]
    features_df[data_skew.index] = np.log1p(features_df[data_skew.index])
    
    # Histogram after skewness reduction
    #myX.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8); # ; avoid having the matplotlib verbose informations
    
    # Missing Data Analysis:
    
    # first we'll visualize null count in overall dataframe
    null_in_HousePrice = features_df.isnull().sum()
    null_in_HousePrice = null_in_HousePrice[null_in_HousePrice > 0]
    null_in_HousePrice.sort_values(inplace=True)
    #null_in_HousePrice.plot.bar()
    
    # Printing total numbers and percentage of missing data
    total = features_df.isnull().sum().sort_values(ascending=False)
    percent = (features_df.isnull().sum()/features_df.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    #print(missing_data.head())
    
    
    # Missing Data Treatment
    
    # Check how many values are missing from each column
    for col in features_df.columns.values:
        missing_values = features_df[col].isnull().sum()
        #print(missing_values)
        
        # Drop if there are too many missing values
        if missing_values > 260:
            features_df = features_df.drop(col, axis = 1)
            
        # If there are fewer than 260 missing values.
        else:
            features_df = features_df.fillna(features_df[col].median())
    #print(myX.describe())
    
    # Histogram after missing data treatment
    #myX.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8)
    
    
    # Exploratory Data Analysis:
    
    ## Scatter plots
    #for col in features_df.columns.values:
        ##print(col)
        #x = features_df[col][features_df[col]>0]
        #y = target[features_df[col]>0]
        #plt.scatter(x,y)
        #plt.ylabel('Sale Price')
        #plt.xlabel(col)
        #plt.show()
    
    ## Pie plot of basement finish:
    ## Pie Plot:
    #labels = ('Finish 1', 'Finish 2', 'Both', 'Neither')
    #BF1 = myX[myX['BsmtFinSF1'] > 0][myX['BsmtFinSF2'] == 0].shape[0]
    #BF2 = myX[myX['BsmtFinSF2'] > 0][myX['BsmtFinSF1'] == 0].shape[0]
    #Both = myX[myX['BsmtFinSF2'] > 0][myX['BsmtFinSF1'] > 0].shape[0]
    #Neither = myX[myX['BsmtFinSF2'] == 0][myX['BsmtFinSF1'] == 0].shape[0]
    #bfSum = BF1 + BF2 + Both + Neither
    #ratio1 = 100.*BF1/bfSum
    #ratio2 = 100.*BF2/bfSum
    #ratioBoth = 100.*Both/bfSum
    #ratioNeither = 100.*Neither/bfSum
    #sizes = [BF1, BF2, Both, Neither]
    #percent = [ratio1, ratio2, ratioBoth, ratioNeither]
    #labels = ['{0} - {1:1.1f} %'.format(i,j) for i,j in zip(labels, percent)]
    
    #colors = ['gold', 'blue', 'green', 'red']
    #patches, texts= plt.pie(sizes, colors=colors, shadow=True, startangle=90)
    #plt.legend(patches, labels, loc='best')
    #plt.title("Basement Finish")
    #plt.show()
    
    
    ## Correlation
    
    ## Plot
    #import matplotlib.pyplot as plt
    #corr=myDF.corr()
    #plt.figure(figsize=(10, 10))
    #ax = sns.heatmap(corr[(corr >= 0.1) | (corr <= -0.1)], 
                #cmap='coolwarm', vmax=0.6, vmin=0, linewidths=0.1,
                #annot=True, annot_kws={"size": 17}, square=True);
    #ax.set_ylim((0,6))
    
    #plt.title('Correlation between features')
    
    # Dropping BsmtFinSF2 due to very weak correlation and limited applicability
    features_df = features_df.drop('BsmtFinSF2', axis=1)
    
    return features_df

