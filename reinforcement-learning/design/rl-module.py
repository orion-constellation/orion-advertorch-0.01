"""
Using RLLib PPO Training Environment to Configure an Agent.

"""
import torch
import pandas as pd
import numpy as np

X = torch.tensor(100,20)
y = torch.tensor(80,20)

dot_product = np.matmul(X, y)
df = pd.DataFrame(dot_product)


def RLLib_Env(df):
    # ENvironment for the agent to be defined and trained in.

    env = NetworkEnv(df)
    config = {
        "env": NetworkEnv,
        "num_workers": 4,
        "lr": 1e-3,
        "gamma": 0.99,
        "framework": "torch",
    }

    # Initialize and train the PPO agent
    trainer = PPOTrainer(config=config)
    for i in range(100):
        result = trainer.train()
        print(f"Iteration: {i}, Reward: {result['episode_reward_mean']}")
        if i % 10 == 0:
            checkpoint = trainer.save()
            print(f"Checkpoint saved at: {checkpoint}")

    ray.shutdown()
    
RLLib_Env(df)
