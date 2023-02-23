"""
This is a boilerplate pipeline 'prediction_pipeline'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import processing_the_test_data, predicting_survival


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=processing_the_test_data,
            inputs=['test_dataset', 'params:test_features', 'params:categorical_features'],
            outputs='df_processed'
        ),
        node(
            func=predicting_survival,
            inputs=['df_processed', 'classification_model'],
            outputs='prediction_dataset'
        ),

    ])
