import os,sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.model_trainer import ModelTrainer

from networksecurity.entity.config_entity import (TrainingPipelineConfig, 
                                                  DataIngestConfig, 
                                                  DataValidationConfig, 
                                                  DataTransformationConfig, 
                                                  ModelTrainerConfig,
                                                  )

from networksecurity.entity.artifact_entity import (DataIngestionArtifact,
                                                    DataValidationArtifact,
                                                    DataTransformationArtifact,
                                                    ModelTrainerArtifact,
                                                    )


class TrainingPipeline:
    
    def __init__(self):
        self.training_pipeline_config=TrainingPipelineConfig
        
    def start_data_ingestion(self):
        try:
            logging.info("data ingestion initiated")
            data_ingestion_config=DataIngestConfig(training_pipeline_config=self.training_pipeline_config)
            data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
            data_ingestion_artifact:DataIngestionArtifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"data ingestion and artifact created:{data_ingestion_artifact}")
            return data_ingestion_artifact
        
        except Exception as e:
            NetworkSecurityException(e,sys)
            
    def start_data_validation(self,data_ingestion_artifact):
        try:
            data_validation_config=DataValidationConfig(self.training_pipeline_config)
            data_validation= DataValidation(data_ingestion_artifact,data_validation_config)
            logging.info("data validation started")
            data_validation_artifact= data_validation.initiate_data_validation()
            logging.info(f"data validation completed and artifact:{data_validation_artifact}")
            return data_validation_artifact
            
        except Exception as e:
            NetworkSecurityException(e,sys)
            
    def start_data_transformation(self,data_validation_artifact):
        try:
            data_transformation_config= DataTransformationConfig(self.training_pipeline_config)
            data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
            logging.info("data transforamtion initiated")
            data_transformation_artifact= data_transformation.initiate_data_transformation()
            logging.info(f"data transformation completed and artifact: {data_transformation_artifact}")
            return data_transformation_artifact
        
        except Exception as e:
            NetworkSecurityException(e,sys)
            
    def start_model_training(self,data_transformation_artifact):
        try:
            model_trainer_config=ModelTrainerConfig(self.training_pipeline_config)
            model_trainer=ModelTrainer(model_trainer_config,data_transformation_artifact)
            logging.info("Model training initiated")
            model_trainer_artifact=model_trainer.initiate_model_trainer()
            logging.info(f"Model trainer artifact created and artifact:{model_trainer_artifact}")
            return model_trainer_artifact
        
        except Exception as e:
            NetworkSecurityException(e,sys)
            

    def run_pipeline(self):
        try:
            self.start_data_ingestion()    
        
        except Exception as e:
            NetworkSecurityException(e,sys)