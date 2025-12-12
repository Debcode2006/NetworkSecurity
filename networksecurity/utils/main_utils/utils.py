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
    
    
def save_numpy_array_data(filepath:str, array:np.array):
    try:
        dir_path = os.path.dirname(filepath)
        os.makedirs(dir_path, exist_ok=True)
        with open(filepath, 'wb') as file:
            np.save(file, array)
            
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
    
def save_object(filepath:str, object:object):
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'wb') as file_obj:
            pickle.dump(object, file_obj)
            
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
    
def load_object(filepath:str)-> object:
    try:
        if not os.path.exists(filepath):
            raise Exception(f"the file {filepath} doesn't exist")
        
        with open(filepath,'rb') as obj:
            print(obj)
            return pickle.load(obj)
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    

def load_numpy_array_data(filepath:str)-> object:
    try:
        if not os.path.exists(filepath):
            raise Exception(f"the file {filepath} doesn't exist")
        with open(filepath,'rb') as obj:
            print(obj)
            return np.load(obj)
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)