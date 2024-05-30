from .model import DecisionModuleModel

import os


default_model = os.path.abspath("./model.joblib")

__all__ = [
    'DecisionModuleModel'
]