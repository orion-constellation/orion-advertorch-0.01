""" 0 is non adversarial
    1 is adversarial
    2 is perhaps adversarial
    
    
    Could also use probabalistic models for a statistical likeihood based on cohort off features.
"""


import os
import pandas as pd
from typing import List, Dict, Tuple
from agents import agent_analysis
from db
from models import TriageAgent

common_threat_protocols = ["ICMP", "DNS"]
#  Set Rate limits (per ms) for both ICMP and DNS which are commonly used to identify hosts or tunnel to command and control
ICMP_LIMIT = 1500 #@TODO ABRITRARY FIGURE - Anomaly detection
DNS_LIMIT = 1500 #TODO Anomaly Detection

def rate_heuristic(data: pd.DataFrame):
    rating = 0
    if data.features['packet_size'] > ICMP_LIMIT and data.features['protocol'] == 'ICMP':
        return rating == 1
    if data.features['packet_size'] > DNS_LIMIT and data.features['protocol'] == "DNS":
        return rating == 1
    elif rating != 1:
        rating == 2
    else:
        rating == 3
        analysis = agent_analysis(rating: int)
        db_store = store_analysis(analysis: JSON)
        return db_store





def main(rating: Tuple, destination: Agents | ):