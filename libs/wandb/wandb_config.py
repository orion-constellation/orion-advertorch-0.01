import logging as _logger
import os
from dotenv import load_dotenv, find_dotenv
try: 
    import wandb 
except ImportError: 
    raise ImportError(
        '“You are trying to use wandb which is not currently installed”
        '“Please install it using pip install wandb”'
    ) 
load_dotenv()

class ConfigWandB:
    """
    Configuration of Weights and Biases for Experiment Tracking and other metrics including
    - RL scenario outcomes.
    
    
    """
    
    def __init__(self, entity: str, wandb_api_key=os.getenv("WANDB_API_KEY")):
        REINIT = True
        SKIP_LOGGING=True
        self.wandb_api_key=wandb_api_key 
        _logger.info("CONFIGURING WANDB")
        
    #@TODO Check project exists or not?  
        wandb.login(key=wandb_api_key)
    #Check if project exists?
        wandb.init(self,project=os.getenv("WANDB_PROJECT"), reinit=REINIT) #@TODO SKIP LOGGING

    @classmethod
    def log_wandb(cls, data):
        return cls.wandb.log(data)
    
    @classmethod    
    def log_artifact(cls, artifact, tmp="./tmp/")
        return cls.wandb.log_artifact(artifact)
    
    @classmethod
    def wandb_sweep_agent(cls,args*, kwargs**):
        cls.config = { } #@TODOSPECIFY
        return wandb.agent()
        



