from us_visa.components.data_ingestion import DataIngestion
from us_visa.entity.config_entity import DataIngestionConfig,DataValidationConfig, DataTransformationConfig
from us_visa.components.data_validation import DataValidation
from us_visa.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from us_visa.components.data_transformation import DataTransformation


### =========================== Data Transfromation =============================
# if __name__ == "__main__":
#     config = DataTransformationConfig()
#     validation_artifact = DataValidationArtifact(validation_status=True, message='Drift not detected',
#                                     drift_report_file_path='artifact\\03_21_2024_21_50_52\\data_validation\\drift_report\\report.yaml')
    
#     ingestion_artifact =  DataIngestionArtifact(trained_file_path='artifact\\03_21_2024_21_49_02\\data_ingestion\\ingested\\train.csv',
#                                  test_file_path='artifact\\03_21_2024_21_49_02\\data_ingestion\\ingested\\test.csv')

#     data_transformation = DataTransformation(ingestion_artifact,
#                                              config,
#                                              validation_artifact)
#     data_transformation.initiate_data_transformation()

#### ============================ Data Validation =============================

# if __name__ == "__main__":
#     config =  DataValidationConfig()
#     obj =  DataIngestionArtifact(trained_file_path='artifact\\03_21_2024_21_49_02\\data_ingestion\\ingested\\train.csv',
#                                  test_file_path='artifact\\03_21_2024_21_49_02\\data_ingestion\\ingested\\test.csv')
#     data_validation = DataValidation(data_ingestion_artifact=obj,
#                    data_validation_config=config)

#     data_validation.initiate_data_validation()


#### ======================== Data Ingestion ================================

if __name__ == "__main__":
    config = DataIngestionConfig()
    data_ingestion = DataIngestion(config)
    data_ingestion.initiate_data_ingestion()




# from us_visa.configuration.mongo_db_connection import MongoDBClient

# MongoDBClient()