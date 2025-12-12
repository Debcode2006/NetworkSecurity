import os,sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.constant.training_pipeline import SAVED_MODEL_DIR, MODEL_FILE_NAME

class NetworkModel:
    def __init__(self, preprocessor, model):
        try:
            self.preprocessor= preprocessor
            self.model=model
            
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    
    def predict(self,x):
        try:
            x_transformed= self.preprocessor.transform(x)
            return self.model.predict(x_transformed)
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        