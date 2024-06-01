from sklearn.metrics import mean_squared_error, mean_absolute_error, accuracy_score, roc_auc_score
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import BaseCrossValidator, BaseShuffleSplit
from sklearn.neighbors import KNeighborsClassifier
from pydantic import BaseModel
from typing import List, Dict, Optional
import pandas as np


class RawData(BaseModel, raw_data):
    payload: json
    uuid: str
    models_tested: Dict
    accuracy_metrics: Dict    

class PreProcess(BaseModel):
    validate: BaseCrossValidator
    shuffle: BaseShuffleSplit
    model_base: KNeighborsClassifier
    
    

class ProduceMetrics(RawData):
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.accuracy_metrics = {"MAE": mean_absolute_error(self.data),  # @TODO FIX THIS SO DATA IS PROCESSED CORRECTLY
                                 "MSE": mean_squared_error(self.data), 
                                 "Acc": accuracy_score(self.data),
                                 "ROC_AUC": roc_auc_score(self.data)}
        
    def preprocess_data(self.raw_data):
        
    
    def evluate_metrics(accuracy_metrics: Dict):


