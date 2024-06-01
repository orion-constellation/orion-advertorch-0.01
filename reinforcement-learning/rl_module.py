import ray
from ray.rllibs.agents.ppo import PPOTrainer
import torch
import pandas as pd
import numpy as np


# We define synthetic data
X = torch.tensor(100,20)
y = torch.tensor(80,20)

# Transform into a  more complex data frame
dot_product = np.matmul(X, y)
df = pd.DataFrame(dot_product)

# @TODO Alex needs to learn more about defining the Gym properly - eg. How is the data used?
class NetworkEnv(gym.Env):
    def __init__(self, data):
        super(NetworkEnv, self).__init__()
        self.data = data
        self.action_space = Discrete(2)  # Two actions: 0 - normal, 1 - alert
        self.observation_space = Box(low=0, high=1, shape=(10,), dtype=np.float32)
        self.state = np.random.rand(10)

    # One step forward
    def step(self, action):
        reward = self.calculate_reward(action) # @TODO Calculate Reward based on RATIO of Accuracy for an unbalanced Dataset eg. F1 Score
        #Lose points for mislabelling a threat etc etc
        done = self.is_done()
        self.state = np.random.rand(10)
        return self.state, reward, done, {}

    # Reset environment
    def reset(self):
        self.state = np.random.rand(10)
        return self.state

    #Calculate reward - Acc vs FP and FN etc
    def calculate_reward(self, action):
        # Reward logic based on action and current state
        return np.random.rand()

    # Finished
    def is_done(self):
        # Termination condition
        return False

    # Main Function
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
        
        # Evaluate the agent
        state = env.reset()
        total_reward = 0
        for _ in range(100):
            action = trainer.compute_action(state)
            state, reward, done, _ = env.step(action)
            total_reward += reward
            if done:
                break
        print(f"Total Reward during evaluation: {total_reward}")


    ray.shutdown()
    
agent = NetworkEnv(self, df)
agent.RLLib_Env(df)
