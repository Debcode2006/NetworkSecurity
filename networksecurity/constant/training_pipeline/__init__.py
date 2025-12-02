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



"""
Data Ingestion related constant
"""
    
DATA_INGESION_COLLECTION_NAME:str = "NetworkData"
DATA_INGESION_DATABASE_NAME:str = "DEBANJANAI"
DATA_INGESION_DIR_NAME:str = "data_ingestion"
DATA_INGESION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESION_INGESTED_DIR:str = "ingested"
DATA_INGESION_TRAIN_TEST_SPLIT_RATIO:float = 0.2