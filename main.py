from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig

from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import DataValidationConfig

from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys

if __name__=='__main__':
    try:
        # Data Ingestion
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)
        
        # Data Validation
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        DataValidation = DataValidation(dataingestionartifact , data_validation_config)
        logging.info("Initiate the data validation")
        data_validation_artifact = DataValidation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(data_validation_artifact)

        
                        
    except Exception as e:
           raise NetworkSecurityException(e,sys)
