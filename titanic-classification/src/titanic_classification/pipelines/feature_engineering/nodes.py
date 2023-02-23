"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.18.4
"""

import pandas as pd


def feature_selection(df: pd.DataFrame, features: list):
    '''
        This function will select the input features and remove the unwanted features from the dataset.
    '''
    df_with_selected_features = df[features]

    return df_with_selected_features

def create_new_features(df_with_selected_features: pd.DataFrame):
    '''
        This node will create a new feature that sums the value of 'SibSp' and 'Parch'
        and returns a new column called 'FamilyMembers'.
    '''

    df_with_new_columns['FamilyMembers'] = df_with_selected_features['SibSp'] + df_with_selected_features['Parch']
    df_with_new_columns = df_with_selected_features.drop(columns = ['SibSp', 'Parch'])

    return df_with_new_columns

def swap_age_null_values_with_average(df_with_new_columns: pd.DataFrame):
    '''
        This node will replace null values on the column 'Age'
        with the average age of the survival group the passenger belongs.

        After that, it will also remove null values from the 'Embarked' column.
    '''
    sobreviveram = df_with_new_columns.query('Survived == 1')
    nao_sobreviveram = df_with_new_columns.query('Survived == 0')

    media_sobreviveram = sobreviveram['Age'].mean()
    sobreviveram['Age'].fillna(value = media_sobreviveram, inplace = True)
    
    media_nao_sobreviveram = nao_sobreviveram['Age'].mean()
    nao_sobreviveram['Age'].fillna(value = media_nao_sobreviveram, inplace = True)

    df_with_average_age = pd.concat([sobreviveram, nao_sobreviveram],ignore_index=True)

    # Removing 2 registries that contain null values on 'Embarked' column.
    df_with_average_age = df_with_average_age[df_with_average_age.Embarked.notnull()]

    return df_with_average_age

def create_dummies(df_with_average_age: pd.DataFrame, categorical_features: list):
    '''
        This node will create dummie columns for the text columns.
    '''

    df_with_dummies = pd.get_dummies(data = df_with_average_age, columns = categorical_features)
    
    return df_with_dummies