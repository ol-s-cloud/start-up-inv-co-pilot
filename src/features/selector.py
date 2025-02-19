from typing import List, Dict, Any
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_classif

class FeatureSelector:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.selected_features = []

    def select_features(self, X: pd.DataFrame, y: pd.Series) -> pd.DataFrame:
        """Select most important features"""
        selector = SelectKBest(score_func=f_classif, k=self.config['n_features'])
        X_selected = selector.fit_transform(X, y)
        self.selected_features = X.columns[selector.get_support()].tolist()
        return pd.DataFrame(X_selected, columns=self.selected_features)