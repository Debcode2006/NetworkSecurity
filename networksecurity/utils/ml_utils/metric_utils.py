from networksecurity.entity.artifact_entity import ClassificationMetricArtifact
from networksecurity.exception.exception import NetworkSecurityException
from sklearn.metrics import f1_score, precision_score,recall_score
import sys

from sklearn.metrics import r2_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier, RandomForestClassifier
from sklearn.model_selection import GridSearchCV

def get_classification_score(y_test, y_pred)-> ClassificationMetricArtifact:
    try:
        model_f1_score= f1_score(y_test, y_pred)
        model_precision_score= precision_score(y_test, y_pred)
        model_recall_score= recall_score(y_test, y_pred)
        
        return ClassificationMetricArtifact(model_f1_score,model_precision_score,model_recall_score)
    
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
    
def evaluate_models(x_train, y_train, x_test, y_test,models,params)-> dict:
    try:
        report={}
        for i in len(list(models)):
            model=list(models.values())[i]
            para=params[list(models.keys())[i]]
            
            gs=GridSearchCV(model,para,cv=3)
            gs.fit(x_train,y_train)
            
            model.set_params(**gs.best_params_)
            model.fit(x_train,y_train)
            
            #y_train_pred=model.predict(x_train)
            y_test_pred=model.predict(x_test)
            
            test_score = r2_score(y_test,y_test_pred)
            
            report[list(models.keys())[i]]=test_score
            
        return report
    
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)