import os, sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))   #interpretor will search in this folder when import is invoked

from src.logger import logging
from src.exception import CustomException
from src.components.data_transformation import DataTransformation, DataTransformationconfig
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
import pandas as pd

@dataclass        #init is not required with this decorator
class DataIngestionConfig:    #for defining inputs required during data ingestion
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config= DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Entered the data ingestion method or component')

        try:
            df= pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok= True)  #create the artifact folder
            
            df.to_csv(self.ingestion_config.raw_data_path, index= False, header= True)

            logging.info('Train test split initiated')
            train_set, test_set= train_test_split(df, test_size= 0.2, random_state= 42)

            train_set.to_csv(self.ingestion_config.train_data_path, index= False, header= True)
            test_set.to_csv(self.ingestion_config.test_data_path, index= False, header= True)

            logging.info('Ingestion of the data in completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)


if __name__== '__main__':
    obj= DataIngestion()
    train_data_path, test_data_path= obj.initiate_data_ingestion()

    data_transformation= DataTransformation()
    data_transformation.initiate_data_transformation(train_data_path, test_data_path)
            

