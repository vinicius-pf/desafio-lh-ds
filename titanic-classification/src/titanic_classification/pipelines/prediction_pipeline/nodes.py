"""
This is a boilerplate pipeline 'prediction_pipeline'
generated using Kedro 0.18.4
"""

import pandas as pd

def processing_the_test_data(df:pd.DataFrame, features:list, categorical_features: list):
    '''
        This node will remove unwanted columns from the testing dataset.
        It will also encode the text features and create the "FamilyMembers" variable.
    '''

    df_with_selected_features = df[features]

    df_with_selected_features['FamilyMembers'] = df_with_selected_features['SibSp'] + df_with_selected_features['Parch']
    df_with_new_columns = df_with_selected_features.drop(columns = ['SibSp', 'Parch'])

    df_processed = pd.get_dummies(data = df_with_new_columns, columns = categorical_features)

    return df_processed

def predicting_survival(df:pd.DataFrame, model):
    '''
        This node will take information on new passengers
        and predict if the passenger will survive or not.
    '''

    prediction = model.predict(df)
    df['Survival_Prediction'] = prediction

    return df