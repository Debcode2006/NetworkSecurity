from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestConfig, TrainingPipelineConfig


import sys


if __name__=='__main__':
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)