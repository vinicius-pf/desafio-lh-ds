"""
This is a boilerplate pipeline 'training_pipeline'
generated using Kedro 0.18.4
"""

import pandas as pd
from xgboost import XGBClassifier


def model_training(df: pd.DataFrame):
    '''
        This node will stance the classification model and 
        ifit it with the pre-processed data.
    '''

    X = df.drop(columns = 'Survived')
    y = df['Survived']

    model = XGBClassifier()
    model.fit(X,y)

    return model
