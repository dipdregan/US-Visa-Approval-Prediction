from us_visa.components.data_ingestion import DataIngestion
from us_visa.entity.config_entity import DataIngestionConfig,DataValidationConfig,\
      DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig,ModelPusherConfig
from us_visa.components.data_validation import DataValidation
from us_visa.components.model_trainer import ModelTrainer
from us_visa.components.model_evaluation import ModelEvaluation
from us_visa.components.model_pusher import ModelPusher
from us_visa.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact,\
    DataTransformationArtifact,ModelTrainerArtifact,ClassificationMetricArtifact,ModelEvaluationArtifact
from us_visa.components.data_transformation import DataTransformation
from us_visa.pipline.training_pipeline import TrainPipeline

#### ================================= Testing the Pipeline ===================
if __name__ =="__main__":
    obj = TrainPipeline()
    obj.run_pipeline()

# ### =================== Model Pusher testing ===================================

# if __name__ == "__main__":
#     config = ModelPusherConfig()
#     artifact = ModelEvaluationArtifact(is_model_accepted=True, 
#                                        changed_accuracy=0.8308339910549855, s3_model_path='model.pkl', 
#                                        trained_model_path='artifact\\03_22_2024_16_21_28\\model_trainer\\trained_model\\model.pkl')
#     obj = ModelPusher(artifact,config)
    

#     obj.initiate_model_pusher()

### ======================== Model Evaluation Testing ====================
# if __name__ == "__main__":
#     config = ModelEvaluationConfig()
#     ingestion =  DataIngestionArtifact(trained_file_path='artifact\\03_22_2024_14_26_23\\data_ingestion\\ingested\\train.csv',
#                                 test_file_path='artifact\\03_22_2024_14_26_23\\data_ingestion\\ingested\\test.csv')
#     trainer = ModelTrainerArtifact(trained_model_file_path='artifact\\03_22_2024_15_06_47\\model_trainer\\trained_model\\model.pkl',
#                                    metric_artifact=ClassificationMetricArtifact(accuracy=0.815070463042853, f1_score=0.8308339910549855, precision_score=0.8562906724511931, recall_score=0.8068472151251916))
#     obj = ModelEvaluation(config,ingestion,trainer)
#     obj.initiate_model_evaluation()


# #### ====================== Model trainer testing ==================
# if __name__ =="__main__":
#     config = ModelTrainerConfig()
#     data_trasnformation_artifact = DataTransformationArtifact(transformed_object_file_path='artifact\\03_22_2024_14_41_33\\data_transformation\\transformed_object\\preprocessing.pkl',
#                                                               transformed_train_file_path='artifact\\03_22_2024_14_41_33\\data_transformation\\transformed\\train.npy', 
#                                                               transformed_test_file_path='artifact\\03_22_2024_14_41_33\\data_transformation\\transformed\\test.npy')

#     model_trainer = ModelTrainer(data_trasnformation_artifact,
#                                  config)
#     model_trainer.initiate_model_trainer()

### =========================== Data Transfromation =============================
# if __name__ == "__main__":
#     config = DataTransformationConfig()
#     validation_artifact = DataValidationArtifact(validation_status=True, message='Drift not detected',
#                                                   drift_report_file_path='artifact\\03_22_2024_14_29_54\\data_validation\\drift_report\\report.yaml')
    
#     ingestion_artifact =  DataIngestionArtifact(trained_file_path='artifact\\03_22_2024_14_26_23\\data_ingestion\\ingested\\train.csv',
#                                                 test_file_path='artifact\\03_22_2024_14_26_23\\data_ingestion\\ingested\\test.csv')

#     data_transformation = DataTransformation(ingestion_artifact,
#                                              config,
#                                              validation_artifact)
#     data_transformation.initiate_data_transformation()

#### ============================ Data Validation =============================

# if __name__ == "__main__":
#     config =  DataValidationConfig()
#     obj =  DataIngestionArtifact(trained_file_path='artifact\\03_22_2024_14_26_23\\data_ingestion\\ingested\\train.csv',
#                                                      test_file_path='artifact\\03_22_2024_14_26_23\\data_ingestion\\ingested\\test.csv')
#     data_validation = DataValidation(data_ingestion_artifact=obj,
#                    data_validation_config=config)

#     data_validation.initiate_data_validation()


#### ======================== Data Ingestion ================================

# if __name__ == "__main__":
#     config = DataIngestionConfig()
#     data_ingestion = DataIngestion(config)
#     data_ingestion.initiate_data_ingestion()




# from us_visa.configuration.mongo_db_connection import MongoDBClient

# MongoDBClient()