""""
NLTK CLASSIFIER INCLUDING PROCESSING OF DATASET AND BASIC MODEL TRAINIGN
- TLDF
"""
import os
from pydantic import BaseModel, HttpUrl, constr
from datetime import datetime
import numpy as np
import pandas as pd
from typing import Optional, List, Dict 
import nltk
from nltk import classify
nltk.download("stopwords")
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer

### INPUT DATA
input_data = [r"^(GET|POST|PUT|DELETE|HEAD|OPTIONS|PATCH)$", r"^(normal|malicious)$"]





class WebTraffic(BaseModel):
    timestamp: datetime
    url: HttpUrl
    method: constr
    status_code: int
    referrer: Optional[HttpUrl]
    user_agent: str
    
def process_reged(input_data):
        df_regex = pd.DataFrame(regex_list, columns=["method", "label"])
        # Apply the regex to the DataFrame in the list 
        df_processed = df_regex.apply(definition_apply)






def main_classifier(dataio):
    web_traffic = WebTraffic()
    web.traffic.apply(dataio)


# Example tokenizer for URLs
tokenizer = RegexpTokenizer(r'[A-Za-z]+')
vectorizer = TfidfVectorizer(tokenizer=tokenizer.tokenize)

# Example URL
apply_regex = [method_apply, label_apply]
tfidf_matrix = vectorizer.fit_transform(apply_regex)

# CONVER TO NUMPY ARRAY
tfidf_matrix = tfidf_matrix.np.toarray()
    


