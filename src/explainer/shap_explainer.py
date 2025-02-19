from typing import Any, Dict
import shap
import numpy as np

class ShapExplainer:
    def __init__(self, model: Any):
        self.model = model
        self.explainer = None

    def fit(self, X: np.ndarray):
        self.explainer = shap.TreeExplainer(self.model)

    def explain(self, X: np.ndarray) -> Dict[str, Any]:
        if self.explainer is None:
            raise ValueError("Explainer not fitted")
        shap_values = self.explainer.shap_values(X)
        return {
            'shap_values': shap_values,
            'expected_value': self.explainer.expected_value
        }