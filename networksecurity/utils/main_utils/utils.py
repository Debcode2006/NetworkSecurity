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