"""
This is a boilerplate pipeline 'training_pipeline'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import model_training


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = model_training,
            inputs={'df':'X'},
            outputs='classification_model'
        )
    ])
