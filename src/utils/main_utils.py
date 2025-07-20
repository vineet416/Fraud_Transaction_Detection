import sys
import os
import pickle
import yaml

from src.constants import *
from src.exception import CustomException
from src.logger import logging


class MainUtils:
    def __init__(self) -> None:
        pass

    def read_yaml_file(self, file_path: str) -> dict:
        """
        Reads a YAML file and returns its content as a dictionary.
        """
        try:
            with open(file_path, 'r') as yaml_file:
                content = yaml.safe_load(yaml_file)
            return content
        
        except Exception as e:
            raise CustomException(e, sys)
        

    @staticmethod
    def save_object(file_path: str, obj: object):
        """
        Saves a Python object to a file using pickle.
        """
        logging.info("Entering save_object method in MainUtils")
        try:
            with open(file_path, 'wb') as file:
                pickle.dump(obj, file)
            logging.info("Exited save_object method in MainUtils")

        except Exception as e:
            raise CustomException(e, sys)


    @staticmethod
    def load_object(file_path: str) -> object:
        """
        Loads a Python object from a file using pickle.
        """
        logging.info("Entering load_object method in MainUtils")
        try:
            with open(file_path, 'rb') as file_obj:
                obj = pickle.load(file_obj)
            logging.info("Exited load_object method in MainUtils")
            return obj
        
        except Exception as e:
            raise CustomException(e, sys)
