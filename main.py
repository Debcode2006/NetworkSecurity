from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestConfig, TrainingPipelineConfig, DataValidationConfig, DataTransformationConfig


import sys


if __name__=='__main__':
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("initiate data ingestion")
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        logging.info("data initiated")
        print(data_ingestion_artifact)
        
        data_validation_config=DataValidationConfig(training_pipeline_config)
        data_validation= DataValidation(data_ingestion_artifact,data_validation_config)
        logging.info("data validation started")
        data_validation_artifact= data_validation.initiate_data_validation()
        logging.info("data validation completed")
        print(data_validation_artifact)
        
        data_transformation_config= DataTransformationConfig(training_pipeline_config)
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        logging.info("data transforamtion initiated")
        data_transformation_artifact= data_transformation.initiate_data_transformation()
        logging.info("data transformation completed")
        print(data_transformation_artifact)
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)