import yaml
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import os, sys
import pandas as pd
import numpy as np
import dill
import pickle

def read_yaml_file(file_path:str)->dict:
    '''
    Reads a YAML file and returns its contents as a dictionary.
    
    Args:
        file_path (str): The path to the YAML file.
    '''
    try:
        with open(file_path, 'rb') as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
def write_yaml_file(file_path:str, content: object, replace: bool = False) -> None:
    '''
    Writes a Python object to a YAML file.
    
    Args:
        file_path (str): The path to the YAML file.
        content (object): The content to write to the file.
        replace (bool): If True, replaces the existing file. Defaults to False.
    '''
    try:
        if replace and os.path.exists(file_path):
            os.remove(file_path)
        with open(file_path, 'w') as file:
            yaml.dump(content, file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)