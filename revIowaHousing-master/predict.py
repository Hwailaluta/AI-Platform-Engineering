import pandas as pd
import numpy as np
from joblib import load
from ordinals import ordinals
from unique.fence import fence_uniq
from unique.cond_2hot import conditions_2hot
from unique.bsmtfn_type import basement_type
import os

path = r'C:\Users\user\Desktop\Revature\Projects\Housing\revIowaHousing-master\\'
os.chdir(path)

df_in = pd.read_csv('test.csv')
df_ID = df_in.Id

df_in.drop(['Id','Utilities','Heating', 'KitchenAbvGr', '3SsnPorch','Exterior2nd','TotalBsmtSF'], axis=1, inplace=True)

df_num, df_obj = ordinals(df_in)

df_fence = fence_uniq(df_in)
df_num = pd.concat([df_num, df_fence], axis=1)

df_cond = conditions_2hot(df_in)
df_num = pd.concat([df_num, df_cond], axis=1)

df_bsmt = basement_type(df_in)
df_num = pd.concat([df_num, df_bsmt], axis=1)

df_obj.drop(['Fence','BsmtFinType1','BsmtFinType2', 'Condition1','Condition2'], axis=1, inplace=True)

df_obj.fillna('None', inplace=True)

### ONE HOT ENCODER ###
enc1h = load('OneHotEnc.joblib')
df_obj = pd.DataFrame(enc1h.transform(df_obj))

### FILL NUMERICS WITH MEDIANS ###
col_medians = load('ColumnMedians.joblib')
df_num.fillna(col_medians, inplace=True)

### HANDLE SKEW ###
df_num_skew = load('SkewCols.joblib')
df_num[df_num_skew] = df_num[df_num_skew].apply(np.log1p)

### FINAL CONCATENATION ###
df_final = pd.concat([df_obj, df_num],axis=1)

### NORMALIZE ###
scaler = load('normalizer.joblib')
np_final = scaler.transform(df_final)

### PCA ###
pcaobj = load('pcaObject.joblib')
np_final = pcaobj.transform(np_final)

ols = load('OLS.joblib')
ridge = load('Ridge.joblib')
sgd = load('SGD.joblib')

predict_ols = pd.Series(ols.predict(np_final)).apply(lambda x: x**2).rename('OLS').map('${:,.2f}'.format)
predict_ridge = pd.Series(ridge.predict(np_final)).apply(lambda x: x**2).rename('Ridge').map('${:,.2f}'.format)
predict_sgd = pd.Series(sgd.predict(np_final)).apply(lambda x: x**2).rename('SGD').map('${:,.2f}'.format)

print(pd.concat([df_ID, predict_ols, predict_ridge, predict_sgd], axis=1))

