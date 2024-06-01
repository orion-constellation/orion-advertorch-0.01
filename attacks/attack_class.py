from models import BaseAttackModel, PGDAttackModel, L2PGDAttackModel, L1PGDAttackModel  # @TODO FINISH

import torch
from torch.nn import nn
from typing import List, Dict, TypedDict
from attacks.attack_dict import advertorch_attacks
from libs.custom_loggers.file_logging import setup_logging

device = "mps" if torch.backends.mps.is_available() else "cpu"

# @TODO ADD DOCSTRINGS AND CLASS SIGNATURES

# Define a TypedDict for the model
class AttackModels(TypedDict):
    PGDAttack: PGDAttackModel
    AttackVectors: attack_dict
    
class AdverTorchAttack(nn.Module):
    def __init__(self, attack: nn.Module, model: nn.Module):
        super().__init__()
        self.attack = attack
        self.model = model

    def forward(self, x, y):
        return self.attack(self.model, x, y)

# Example implementation of a PGD attack
class ExamplePGDAttack(nn.Module):
    def __init__(self, epsilon: float, alpha: float, iterations: int):
        super().__init__()
        self.epsilon = epsilon
        self.alpha = alpha
        self.iterations = iterations
        

    def forward(self, model, x, y):
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

def execute_iterations(attack: AdverTorchAttack, data_loader: torch.utils.data.DataLoader, device: torch.device):
    attack.to(device)
    for x, y in data_loader:
        x, y = x.to(device), y.to(device)
        perturbed_x = attack(x, y)
        # Further processing or evaluation of the perturbed inputs
        # For example, evaluating the model's performance on perturbed data
        output = attack.model(perturbed_x)
        pred = output.argmax(dim=1)
        accuracy = (pred == y).float().mean()
        print(f"Accuracy on perturbed data: {accuracy.item() * 100:.2f}%")


def main():
    # Init nice logger
    _logger = setup_logging()
    # Dummy data loader for testing
    dummy_data_loader = torch.utils.data.DataLoader(
        [(torch.rand(784), torch.tensor(0)) for _ in range(100)], batch_size=10
    )

    # Execute iterations with the attack
    execute_iterations(adver_torch_attack, dummy_data_loader, device=device)
    

if __name__==__main__:
    try:
        main()
        _logger.info("Successfully init attack")
    except Exception as e:
        _logger.error("Error, failed to init {}", e)