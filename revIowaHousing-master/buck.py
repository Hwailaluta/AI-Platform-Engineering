import pandas as pd

def feature_extract(df:pd.DataFrame) -> pd.DataFrame:
    """Only extracts the ScreenPorch feature due to lack of correlation in other features."""
    features = df[['EnclosedPorch', 'ScreenPorch']]
    return features
