import os,sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
import networksecurity.constant.training_pipeline
from networksecurity.entity.artifact_entity import DataTransformationArtifact,DataValidationArtifact
from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.utils.main_utils.utils import save_numpy_array_data, save_object

class DataTransformation:
    def __init__(self, data_validation_artifact:DataValidationArtifact, data_transformation_config:DataTransformationConfig):
        try:
            self.data_validation_artifact=data_validation_artifact
            self.data_transformation_config=data_transformation_config
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    
    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    
    def initiate_data_transformation(self)-> DataTransformationArtifact:
        logging.info("entered iniiate_data_transformation")
        try:
            logging.info("initiated data transformaion")
            train_df = DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)