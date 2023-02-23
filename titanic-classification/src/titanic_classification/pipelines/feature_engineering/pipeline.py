"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import select_features, create_new_features, swap_age_null_values_with_average, create_dummies


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = select_features,
            inputs=['training_dataset', 'params:features'],
            outputs='df_with_selected_features'
        ),
        node(
            func = create_new_features,
            inputs=['df_with_selected_features'],
            outputs='df_with_new_columns'
        ),
        node(
            func = swap_age_null_values_with_average,
            inputs=['df_with_new_columns'],
            outputs='df_with_average_age'
        ),
        node(
            func = create_dummies,
            inputs=['df_with_new_columns','params:categorical_features'],
            outputs='X'
        ),     
    ])
