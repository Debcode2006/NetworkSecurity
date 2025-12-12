import os
import sys
import pandas as pd
import numpy as np

"""
defining common constant variables
"""
TARGET_COLUMN = "Result"
PIPELINE_NAME:str = "NetworkSecurity"
ARTIFACT_NAME:str = "Artifacts"
FILE_NAME:str = "phisingData.csv"

TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"

SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")

SAVED_MODEL_DIR= os.path.join("saved_models")
MODEL_FILE_NAME= 'model.pkl'
"""
Data Ingestion related constant
"""
    
DATA_INGESION_COLLECTION_NAME:str = "NetworkData"
DATA_INGESION_DATABASE_NAME:str = "DEBANJANAI"
DATA_INGESION_DIR_NAME:str = "data_ingestion"
DATA_INGESION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESION_INGESTED_DIR:str = "ingested"
DATA_INGESION_TRAIN_TEST_SPLIT_RATIO:float = 0.2

"""
Data Validation related constant
"""
DATA_VALIDATION_DIR_NAME:str= "data_validation"
DATA_VALIDATION_VALID_DIR:str= "validated"
DATA_VALIDATION_INVALID_DIR:str= "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR:str= "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str= "report.yaml"


"""
Data Transformation related constant
"""
DATA_TRANSFORMATION_DIR_NAME:str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"

DATA_TRANSFORMATION_IMPUTER_PARAMS:dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights":"uniform",
}

"""
Model trainer related constants
"""
MODEL_TRAINER_DIR:str="model_tainer"
MODEL_TRAINER_TRAINED_MODEL_DIR:str="trained_model"
EXPECTED_ACCURACY:float=0.6
MODEL_TRAINER_TRAINED_MODEL_NAME:str="model.pkl"
MODEL_TRAINER_OVERFITTING_UNDERFITTING_THRESHOLD:float= 0.05