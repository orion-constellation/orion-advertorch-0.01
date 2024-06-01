# Reinforcement learning with Ray and measured by Weave
from typing import List, Dict, Any, Optional
import ray
from ray import tune, serve
import pandas as pd
import mlflow
from mlflow.tracking import MlflowClient
import wandb
from wandb.integration.ray import WandbLoggerCallback
from pydantic import BaseModel 
from file_logging import setup_logging
import nltk
from nltk import classify
nltk.download(classify)


# Setup Logging
logger = setup_logging()


# Initialize Ray, MLflow, and WandB
ray.init(ignore_reinit_error=True)
mlflow.set_tracking_uri("http://localhost:5000")
wandb.init(project='Orion_RLLib_Project', entity='your_wandb_entity')

# Setup Weave integration
weave = wandb.Api().weave()

# Orion Data Stream Simulation
def simulate_orion_data(raw_data: BaseModel(Dict)):
    # Simulated data
    received_data: Dict =raw_data 
    features: List = []
    # Enumerate the features in the data based on a previous criteria
    enum_list = enumerate(features)
    logger.debug(enum_list)
    df_data = pd.DataFrame(enum_list)
    
    nltk.classify()
    
    
    
    
    
    
    
    data = {'feature1': [0.1, 0.2, 0.3], 'feature2': [1, 2, 3], 'action': [0, 1, 0], 'reward': [1, 0, -1]}
    return data

def process_rx_data(raw_data: Dict):

# RLLib Training Function with MLOps Integration
def train_rl_model(data):
    config = {
        "env": "CartPole-v1",
        "num_workers": 1,
        "framework": "torch",
        "lr": tune.grid_search([0.01, 0.001])
    }

    # Start an MLflow run
    with mlflow.start_run():
        # Ray Tune with MLflow and WandB logging
        analysis = tune.run(
            "PPO",
            config=config,
            stop={"training_iteration": 10},
            callbacks=[WandbLoggerCallback(), tune.integration.mlflow.MLflowLoggerCallback()]
        )
        best_model = analysis.get_best_model("episode_reward_mean")

        # Log model in MLflow
        mlflow.pytorch.log_model(best_model, "model")
        mlflow.end_run()

        # Register model with Weave for version control and data workflow tracking
        weave.register_model(best_model, "rl_model", project="Orion_RLLib_Project")

    return best_model

# Ray Serve Deployment
class RLModelServe:
    def __init__(self, model):
        self.model = model

    async def __call__(self, request):
        json_input = await request.json()
        input_df = pd.DataFrame([json_input])
        action = self.model.compute_action(input_df)
        return {"action": action}

# Deployment with MLflow and Weave
def deploy_model(model):
    serve.start()
    serve.create_backend("rl_model_backend", RLModelServe, model)
    serve.create_endpoint("rl_model_endpoint", backend="rl_model_backend", route="/predict")

# Main Pipeline Execution
if __name__ == "__main__":
    live_data = simulate_orion_data()
    trained_model = train_rl_model(live_data)
    deploy_model(trained_model)
