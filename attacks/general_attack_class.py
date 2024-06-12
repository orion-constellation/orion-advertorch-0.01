"""
An attempt to unify the framework to accept all model types either pretrained or which will undergo
training as part of the execution of the attack.

It will also take in to account the existing Advertorch attack vectors

NOTE TO ALEX: MAYBE DO DEFENSIVE SHIT TOO  Hhahahahahah..... "Offensive-Defensive AI"





"""
import os 
import sys
import argsparser 
import torch
from torch import nn
from torch.nn import Module
from torch.nn.functional import Functional as F #TODO FIX ME!

# preprocessing dependencies
from advertorch.utils import predict_from_logits
from advertorch_examples.utils import ImageNetClassNameLookup
from advertorch_examples.utils import get_panda_image
from advertorch_examples.utils import bhwc2bchw
from advertorch_examples.utils import bchw2bhwc
 
# load the attack class

class GeneralAttackClass(nn.Module):
    """
    epsilon: variance, alpha: Normalisation, epoch
    
    
    """
    def __init__(self, epsilon: float, alpha: float, epochs: int, victim_model: nn.Module):
        super().__init__()
        self.epsilon = epsilon
        self.alpha = alpha
        self.epochs = epochs
        self.victim_model = model
    
    

    def forward(self, model, x, y) -> nn.Module:
        # Example PGD attack logic
        perturbed_x = x.clone().detach().requires_grad_(True)
        for _ in range(self.iterations):
            output = model(perturbed_x)
            loss = nn.CrossEntropyLoss()(output, y)
            loss.backward()
            with torch.no_grad():
                perturbed_x = perturbed_x + self.alpha * perturbed_x.grad.sign()
                perturbed_x = torch.clamp(perturbed_x, x - self.epsilon, x + self.epsilon)
                perturbed_x = torch.clamp(perturbed_x, 0, 1)  # assuming input is normalized
            perturbed_x.grad.zero_()
        return perturbed_x

# Example usage
model = nn.Sequential(nn.Linear(784, 256), nn.ReLU(), nn.Linear(256, 10))  # Dummy model
pgd_attack = ExamplePGDAttack(epsilon=0.3, alpha=0.01, iterations=40)

adver_torch_attack = AdverTorchAttack(attack=pgd_attack, model=model)
 
device = "cuda" if torch.cuda.is_available() else "cpu"

class UniversalAttackkModule
