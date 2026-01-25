import sys
import numpy as np
import pandas as pd
import os
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from networksecurity.constant.training_pipeline import TARGET_COLUMN
from networksecurity.constant.training_pipeline import DATA_TRANSFORMATION_IMPUTER_PARAMS

from networksecurity.entity.artifact_entity import DataTransformationArtifact, DataValidationArtifact
from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.utils.main_utils.utils import save_numpy_array_data, save_object

class DataTransformation:
    def __init__(self,data_validation_artifact: DataValidationArtifact,
                 data_transformation_config: DataTransformationConfig):
        try:
            logging.info(f"{'>>'*20}Data Transformation log started.{'<<'*20} ")
            self.data_transformation_config:DataTransformationConfig = data_transformation_config
            self.data_validation_artifact:DataValidationArtifact = data_validation_artifact
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    @staticmethod
    def read_data(file_path:str)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def get_data_transformer_object(cls)->Pipeline:
        '''
        It initialises a knn imputer object with the parameters specified in the training_pipeline.py file
         and then creates a pipeline with the KNN Imputer object as first step
        
         :param cls: Description
        
        :param cls: Description
        :return: Description
        :rtype: Pipeline
        '''

        logging.info(f"Creating data transformer object")
        try:
            KNNImputer_params = DATA_TRANSFORMATION_IMPUTER_PARAMS
            knn_imputer = KNNImputer(**KNNImputer_params)

            logging.info(f"Created KNN Imputer object with params: {KNNImputer_params}")

            preprocessor = Pipeline(steps=[
                ('imputer', knn_imputer)
            ])

            return preprocessor
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

        
    def initiate_data_transformation(self)-> DataTransformationArtifact:
        logging.info(f"Entering data transformation")
        try:
            logging.info(f"starting data transformation")

            # reading training and testing file
            train_df = DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df = DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)

            # training dataframe
            imput_feature_train_df = train_df.drop(columns=[TARGET_COLUMN],axis=1)
            target_feature_train_df = train_df[TARGET_COLUMN]
            target_feature_train_df = target_feature_train_df.replace(-1,0)

            # testing dataframe
            imput_feature_test_df = test_df.drop(columns=[TARGET_COLUMN],axis=1)
            target_feature_test_df = test_df[TARGET_COLUMN]
            target_feature_test_df = target_feature_test_df.replace(-1,0)

            # data transformation
            preprocessing = self.get_data_transformer_object()
            preprocessor_object = preprocessing.fit(imput_feature_train_df)

            transformed_imput_train_feature = preprocessor_object.transform(imput_feature_train_df)
            transformed_imput_test_feature = preprocessor_object.transform(imput_feature_test_df)
            
            train_arr = np.c_[transformed_imput_train_feature, np.array(target_feature_train_df)]
            test_arr = np.c_[transformed_imput_test_feature, np.array(target_feature_test_df)]

            # save numpy array
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path, array=train_arr)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path, array=test_arr)

            # save preprocessor object pickle file
            save_object(self.data_transformation_config.transformed_object_file_path, preprocessor_object)
            save_object("final_model/preprocessor.pkl",preprocessor_object,)

            # prepare artifact
            data_transformation_artifact = DataTransformationArtifact(
                transformed_train_file_path = self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path = self.data_transformation_config.transformed_test_file_path,
                transformed_object_file_path = self.data_transformation_config.transformed_object_file_path
            )

            logging.info(f"Data transformation artifact: {data_transformation_artifact}")
            return data_transformation_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)
           