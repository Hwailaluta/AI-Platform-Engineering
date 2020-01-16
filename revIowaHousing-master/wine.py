#@author: winegardner
""" """
import pandas as pd
def feature_extract(data:pd.DataFrame):
   """Converting Na to 0 for FireplaceQu,GarageType,GarageFinish"""
   data['FireplaceQu'].fillna(0, inplace=True)
   data['GarageType'].fillna(0, inplace=True)
   data['GarageFinish'].fillna(0, inplace=True)
   """Categorical Features converted to ordinals."""
   # features = data[['Functional', 'FireplaceQu','GarageType','GarageFinish']]
   data.loc[data['Functional']=='Typ','Functional'] = 0
   data.loc[data['Functional']=='Min1','Functional'] = 1
   data.loc[data['Functional']=='Min2','Functional'] = 2
   data.loc[data['Functional']=='Mod','Functional'] = 3
   data.loc[data['Functional']=='Maj1','Functional'] = 4
   data.loc[data['Functional']=='Maj2','Functional'] = 5
   data.loc[data['Functional']=='Sev','Functional'] = 6
   data.loc[data['Functional']=='Svg','Functional'] = 7
   data.loc[data['FireplaceQu']=='Po','FireplaceQu'] = 1
   data.loc[data['FireplaceQu']=='Fa','FireplaceQu'] = 2
   data.loc[data['FireplaceQu']=='TA','FireplaceQu'] = 3
   data.loc[data['FireplaceQu']=='Gd','FireplaceQu'] = 4
   data.loc[data['FireplaceQu']=='Ex','FireplaceQu'] = 5
   data.loc[data['FireplaceQu']=='Sev','FireplaceQu'] = 6
   data.loc[data['GarageType']=='CarPort','GarageType'] = 1
   data.loc[data['GarageType']=='2Types','GarageType'] = 2
   data.loc[data['GarageType']=='Basment','GarageType'] = 3
   data.loc[data['GarageType']=='Detchd','GarageType'] = 4
   data.loc[data['GarageType']=='Builtin','GarageType'] = 5
   data.loc[data['GarageType']=='Attchd','GarageType'] = 6
   data.loc[data['GarageFinish']=='Unf','GarageFinish'] = 1
   data.loc[data['GarageFinish']=='RFn','GarageFinish'] = 2
   data.loc[data['GarageFinish']=='Fin','GarageFinish'] = 3
   return data[['Functional', 'FireplaceQu','GarageType','GarageFinish']]

   

    
   



