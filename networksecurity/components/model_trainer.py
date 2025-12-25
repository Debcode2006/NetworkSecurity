import os, sys
import numpy as np
import mlflow
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.artifact_entity import ModelTrainerArtifact, DataTransformationArtifact, ClassificationMetricArtifact
from networksecurity.entity.config_entity import ModelTrainerConfig
from networksecurity.constant import training_pipeline

from networksecurity.utils.main_utils.utils import load_numpy_array_data, save_object, load_object
from networksecurity.utils.ml_utils.metric_utils import get_classification_score, evaluate_models
from networksecurity.utils.ml_utils.model.estimator import NetworkModel

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier, RandomForestClassifier

class ModelTrainer:
    def __init__(self, model_trainer_config:ModelTrainerConfig, data_transformation_artifact: DataTransformationArtifact):
        try:
            self.model_trainer_config=model_trainer_config
            self.data_transformation_artifact= data_transformation_artifact
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
        
    def track_mlflow(self,model,classificationmetric:ClassificationMetricArtifact):
        with mlflow.start_run():
            f1_score= classificationmetric.f1_score
            precision_score=classificationmetric.precision_score
            recall_score=classificationmetric.recall_score
            
            mlflow.log_metric("f1 score",f1_score)
            mlflow.log_metric("precision score",precision_score)
            mlflow.log_metric("recall score",recall_score)
            mlflow.sklearn.log_model(model,"model")
    
        
    def train_model(self,x_train,y_train,x_test,y_test):
        try:
            models={
                "Random Forest":RandomForestClassifier(verbose=1),
                "Decision Tree": DecisionTreeClassifier(),
                "Logistic Regression": LogisticRegression(verbose=1),
                #"KNN Classifier":KNeighborsClassifier(),
                "AdaBoost":AdaBoostClassifier(),
                "Gradient Boost":GradientBoostingClassifier(verbose=1),
            }
            params={
                "Decision Tree": {
                    'criterion':['gini', 'entropy', 'log_loss'],
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt','log2'],
                },
                "Random Forest":{
                    # 'criterion':['gini', 'entropy', 'log_loss'],
                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,128,256]
                },
                "Gradient Boost":{
                    # 'loss':['log_loss', 'exponential'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.85,0.9],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Logistic Regression":{},
                "AdaBoost":{
                    'learning_rate':[.1,.01,.001],
                    'n_estimators': [8,16,32,64,128,256]
                }        
            }
            model_report:dict= evaluate_models(x_train,y_train,x_test,y_test,models, params)
            best_model_score=max(list(model_report.values()))
            best_model_name= list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            
            best_model=models[best_model_name]
            
            y_train_pred=best_model.predict(x_train)
            train_classification_score=get_classification_score(y_train, y_train_pred)
            
            self.track_mlflow(best_model, train_classification_score)
            
            y_test_pred=best_model.predict(x_test)
            test_classification_score=get_classification_score(y_test, y_test_pred)
            
            self.track_mlflow(best_model, train_classification_score)

            
            prepocessor= load_object(filepath=self.data_transformation_artifact.transformed_object_file_path)
            os.makedirs(os.path.dirname(self.model_trainer_config.trained_model_file_path), exist_ok=True)
            
            Network_model = NetworkModel(prepocessor,best_model)
            save_object(self.model_trainer_config.trained_model_file_path,object=Network_model)
            
            save_object("final_model/model.pkl",best_model)
            
            logging.info("trained model artifact created.")
            return ModelTrainerArtifact(trained_model_file_path=self.model_trainer_config.trained_model_file_path,
                                 train_metric_artifact=train_classification_score,
                                 test_metric_artifact=test_classification_score)
            
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    
    def initiate_model_trainer(self)-> ModelTrainerArtifact:
        try:
            train_file_path= self.data_transformation_artifact.transformed_train_file_path
            test_file_path= self.data_transformation_artifact.transformed_test_file_path
            
            train_arr = load_numpy_array_data(train_file_path)
            test_arr = load_numpy_array_data(test_file_path)
            
            x_train, y_train, x_test, y_test= (train_arr[:,:-1], train_arr[:,-1], test_arr[:,:-1], test_arr[:,-1])
            
            trained_model_artifact=self.train_model(x_train,y_train,x_test,y_test)
            return trained_model_artifact
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)

