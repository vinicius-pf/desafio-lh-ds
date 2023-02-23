"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from titanic_classification.pipelines import feature_engineering, training_pipeline


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """

    feature_engineering_pipeline = feature_engineering.create_pipeline()
    model_trainig_pipeline = training_pipeline.create_pipeline()

    #pipelines = find_pipelines()
    #pipelines["__default__"] = sum(pipelines.values())

    
    return {
        'feature_engineering': feature_engineering_pipeline,
        'model_training': model_trainig_pipeline,
        "__default__": (
            feature_engineering_pipeline
             + model_trainig_pipeline
        )
    }