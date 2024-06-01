from pydantic import BaseModel
from typing import List, Dict, Optional, Object 
from attack_dict import advertorch_attacks
from torch import Adam, SGD
from 

from pydantic import BaseModel, Field
from typing import Optional


class BaseAttackModel(BaseModel):
    description: Optional[str] = Field(None, description="Description of the attack.")
    epochs: int
    optimizer: ["Adam": str, "SGD": str]
    layers: List(Str)


class GradientAttackModel(BaseAttackModel):
    learning_rate: float = Field(0.01, description="Learning rate for the attack.")
    max_iterations: int = Field(1000, description="Maximum number of iterations for the attack.")


class GradientAttackSignModel(BaseAttackModel):
    learning_rate: float = Field(0.01, description="Learning rate for the attack.")
    max_iterations: int = Field(1000, description="Maximum number of iterations for the attack.")


class FastFeatureAttackModel(BaseAttackModel):
    epsilon: float = Field(0.3, description="Perturbation magnitude for the attack.")


class L2BasicIterativeAttackModel(BaseAttackModel):
    epsilon: float = Field(0.3, description="Perturbation magnitude for the attack.")
    alpha: float = Field(0.01, description="Step size for the attack.")
    iterations: int = Field(40, description="Number of iterations for the attack.")


class LinfBasicIterativeAttackModel(BaseAttackModel):
    epsilon: float = Field(0.3, description="Perturbation magnitude for the attack.")
    alpha: float = Field(0.01, description="Step size for the attack.")
    iterations: int = Field(40, description="Number of iterations for the attack.")


class PGDAttackModel(BaseAttackModel):
    epsilon: float = Field(0.3, description="Perturbation magnitude for the attack.")
    alpha: float = Field(0.01, description="Step size for the attack.")
    iterations: int = Field(40, description="Number of iterations for the attack.")


class L2PGDAttackModel(BaseAttackModel):
    epsilon: float = Field(0.3, description="Perturbation magnitude for the attack.")
    alpha: float = Field(0.01, description="Step size for the attack.")
    iterations: int = Field(40, description="Number of iterations for the attack.")


class L1PGDAttackModel(BaseAttackModel):
    epsilon: float = Field(0.3, description="Perturbation magnitude for the attack.")
    alpha: float = Field(0.01, description="Step size for the attack.")
    iterations: int = Field(40, description="Number of iterations for the attack.")


class LinfSPSAAttackModel(BaseAttackModel):
    epsilon: float = Field(0.3, description="Perturbation magnitude for the attack.")
    delta: float = Field(0.01, description="Perturbation size for the attack.")
    iterations: int = Field(40, description="Number of iterations for the attack.")


class FABAttackModel(BaseAttackModel):
    n_restarts: int = Field(5, description="Number of restarts for the attack.")
    n_iter: int = Field(100, description="Number of iterations for the attack.")


class LinfFABAttackModel(BaseAttackModel):
    n_restarts: int = Field(5, description="Number of restarts for the attack.")
    n_iter: int = Field(100, description="Number of iterations for the attack.")


class L2FABAttackModel(BaseAttackModel):
    n_restarts: int = Field(5, description="Number of restarts for the attack.")
    n_iter: int = Field(100, description="Number of iterations for the attack.")


class L1FABAttackModel(BaseAttackModel):
    n_restarts: int = Field(5, description="Number of restarts for the attack.")
    n_iter: int = Field(100, description="Number of iterations for the attack.")


class SparseL1DescentAttackModel(BaseAttackModel):
    epsilon: float = Field(0.3, description="Perturbation magnitude for the attack.")
    iterations: int = Field(40, description="Number of iterations for the attack.")


class MomentumIterativeAttackModel(BaseAttackModel):
    epsilon: float = Field(0.3, description="Perturbation magnitude for the attack.")
    alpha: float = Field(0.01, description="Step size for the attack.")
    iterations: int = Field(40, description="Number of iterations for the attack.")


class LinfMomentumIterativeAttackModel(BaseAttackModel):
    epsilon: float = Field(0.3, description="Perturbation magnitude for the attack.")
    alpha: float = Field(0.01, description="Step size for the attack.")
    iterations: int = Field(40, description="Number of iterations for the attack.")


class L2MomentumIterativeAttackModel(BaseAttackModel):
    epsilon: float = Field(0.3, description="Perturbation magnitude for the attack.")
    alpha: float = Field(0.01, description="Step size for the attack.")
    iterations: int = Field(40, description="Number of iterations for the attack.")


class CarliniWagnerL2AttackModel(BaseAttackModel):
    confidence: float = Field(0.0, description="Confidence level for the attack.")
    learning_rate: float = Field(0.01, description="Learning rate for the attack.")
    binary_search_steps: int = Field(9, description="Number of binary search steps for the attack.")


class ElasticNetL1AttackModel(BaseAttackModel):
    confidence: float = Field(0.0, description="Confidence level for the attack.")
    learning_rate: float = Field(0.01, description="Learning rate for the attack.")
    binary_search_steps: int = Field(9, description="Number of binary search steps for the attack.")


class DDNL2AttackModel(BaseAttackModel):
    steps: int = Field(100, description="Number of steps for the attack.")
    gamma: float = Field(0.1, description="Gamma parameter for the attack.")


class LBFGSAttackModel(BaseAttackModel):
    epsilon: float = Field(0.3, description="Perturbation magnitude for the attack.")
    max_iterations: int = Field(100, description="Maximum number of iterations for the attack.")


class SinglePixelAttackModel(BaseAttackModel):
    max_iterations: int = Field(100, description="Maximum number of iterations for the attack.")


class LocalSearchAttackModel(BaseAttackModel):
    max_iterations: int = Field(100, description="Maximum number of iterations for the attack.")


class SpatialTransformAttackModel(BaseAttackModel):
    max_iterations: int = Field(100, description="Maximum number of iterations for the attack.")


class JacobianSaliencyMapAttackModel(BaseAttackModel):
    theta: float = Field(0.1, description="Theta parameter for the attack.")
    gamma: float = Field(0.1, description="Gamma parameter for the attack.")
    

class AttackResponse(BaseModel):
    success: bool
    message: Json(AttackResponseMessage)
    