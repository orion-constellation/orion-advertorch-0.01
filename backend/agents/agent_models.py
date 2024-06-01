from pydantic import BaseModel
from typing import List, Dict, Optional, Object, JSON
from attacks.attack_dict import advertorch_attacks
from torch.optimizers import Adam, SGD #@TODO FIX
from uuid import uuidv4

from pydantic import BaseModel, Field
from typing import Optional

MAX_ITERATIONS = 5

class BaseAgentModel(BaseModel):
    uuid: uuidv4
    description: Optional[str] = Field(None, description="Description of the attack.")
    max_iterations: MAX_ITERATIONS
    api_keys: #@TODO USE CONFIG FILE?


class TriageAgent(BaseAgentModel):
    minimum_conf_int: 0.90
    tools: List 
    
class CommsAgent(BaseAgentModel):
    enc_algo = #@TODO ADD ENC ALGO
    data_raw: Dict
    data_processed: JSON #@TODO NEED FUNCTION 
    data_reporting: BaseAgentModel
    uri_base_path:f"{uri}/api/v1/"
    
    
    