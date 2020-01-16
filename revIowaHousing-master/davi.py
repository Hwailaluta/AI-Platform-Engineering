import pandas as pd

def feature_extract(df:pd.DataFrame) -> pd.DataFrame:
  """Extracts 'Fireplaces', 'HalfBath', 'BedroomAbvGr', 'TotRmsAbvGrd' where 
  KitchenAbvGr is excluded due to its negative correlation to sale price being inversely related to proper sales price predictions"""
  features = df[['Fireplaces', 'HalfBath', 'BedroomAbvGr', 'TotRmsAbvGrd', 'KitchenAbvGr']]

  """ Data Review
  Check for nan values = none
  Check for outliers = none
  Kurtosis and Skew Review:
  Fireplaces Kurt:  -0.21723720752814657
  Fireplaces Skew:  0.6495651830548841

  HalfBath Kurt:  -1.0769272841476227
  HalfBath Skew:  0.675897448233722

  BedroomAbvGr Kurt:  2.230874582191236
  BedroomAbvGr Skew:  0.21179009627507137

  KitchenAbvGr Kurt:  21.532403840138784
  KitchenAbvGr Skew:  4.488396777072859

  TotRmsAbvGrd Kurt:  0.8807615657189474
  TotRmsAbvGrd Skew:  0.6763408364355531

  Attempts to reduce the skew were unsuccessful possibly due to the value limitations
  """
        
  return features
