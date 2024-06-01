import gym
from gym.spaces import Discrete, Box
from torch.nn import trainer
import numpy as np
from libs.custom_loggers.file_logging import setup_logging


class NetworkEnv(gym.Env):
    _logger = setup_logging()
    def __init__(self):
        super(NetworkEnv, self).__init__()
        self.action_space = Discrete(2) # 0 - Normal, 1 - Alert
        self.observation_space = Box(low=0, high=1, shape=(10,),
                                    dtype=np.float32)
        self.state = np.random.rand(10) #Possible states for the system
        _logger.info("initialized")
        
    def step(self, action):
        reward = self.calculate_reward(action)
        self.state += reward
        done = self.is_done()
        self.state = np.random.rand(10)
        return self.state, reward, done, {}
    
    def reset(self, state):
        self.state = np.random.rand(10)
        return self.state
    
    def calculate_reward(self, action):
        for ix in range(50):
            self.current_reward = step(self, self.state[ix])
            if self.state < 10:
                self.state += 1
                self.step(self, self.state)
                self.state +=1
            elif self.state -= 1:
            self.curent_reward = self.reset(self, self.action_space)
        if self.reward <= 3:
            return np.random.rand()
    
    def is_done(self):
        if self.state != 10:
            return False
        return True
    
    def train_agent(trainer = PPOTrainer(config=config), iterations=100):    
        for i in range(iterations):
            result = trainer.train()
            print(f"Iteration: {i}, Reward: {result['episode_reward_mean']}")
            if i % 10 == 0:
                checkpoint = trainer.save()
                _logger.info(f"Checkpoint saved at: {checkpoint}")   
        
    '''def main(initial_state=self.reset(self, state)):
        env = NetworkEnv()
        while env.is_done != True:
            env.calculate_reward(self, (self.state += 1))
            env.step(env.state += 1)'''


if __name__==__main__(self):
    main()
