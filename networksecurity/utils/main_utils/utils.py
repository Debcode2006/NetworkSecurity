import yaml
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import os,sys
import pickle
import numpy as np

def read_yaml_file(filepath:str)-> dict:
    try:
        with open(filepath, "rb") as yaml_obj:
            return yaml.safe_load(yaml_obj)
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
def write_yaml_file(filepath:str, content:object, replace:bool=False)-> dict:
    try:
        if replace:
            if os.path.exists(filepath):
                os.remove(filepath)
            os.makedirs(os.path.dirname(filepath),exist_ok=True)
        with open(filepath, "w") as yaml_obj:
            return yaml.safe_dump(content, yaml_obj)
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)