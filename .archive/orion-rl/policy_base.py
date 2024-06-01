"""Policy Development:
- Define how your policy computes actions from observations
- Implement learning/update logic here

"""

from ray.rllib.policy import Policy

class CustomPolicy(Policy):
    def __init__(self, observation_space, action_space, config):
        super().__init__(observation_space, action_space, config)

    def compute_actions(self, obs_batch, **kwargs):
        
        return [action_space.sample() for _ in obs_batch], [], {}

    def learn_on_batch(self, samples):
        
        return {}
    
    