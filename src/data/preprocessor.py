from typing import Dict, Any, Tuple
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

class DataPreprocessor:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.scalers = {}

    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        """Preprocess the dataset"""
        df = df.copy()
        
        # Handle missing values
        df = self._handle_missing_values(df)
        
        # Scale numerical features
        df = self._scale_features(df)
        
        # Encode categorical features
        df = self._encode_categorical(df)
        
        return df

    def _handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Handle missing values based on config"""
        strategy = self.config.get('missing_value_strategy', 'mean')
        for column in df.columns:
            if df[column].isnull().any():
                if strategy == 'mean':
                    df[column].fillna(df[column].mean(), inplace=True)
                elif strategy == 'median':
                    df[column].fillna(df[column].median(), inplace=True)
                elif strategy == 'mode':
                    df[column].fillna(df[column].mode()[0], inplace=True)
        return df

    def _scale_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Scale numerical features"""
        numerical_features = self.config.get('numerical_features', [])
        scaling_strategy = self.config.get('scaling_strategy', 'standard')
        
        for feature in numerical_features:
            if feature in df.columns:
                if scaling_strategy == 'standard':
                    scaler = StandardScaler()
                elif scaling_strategy == 'minmax':
                    scaler = MinMaxScaler()
                
                df[feature] = scaler.fit_transform(df[[feature]])
                self.scalers[feature] = scaler
        
        return df

    def _encode_categorical(self, df: pd.DataFrame) -> pd.DataFrame:
        """Encode categorical features"""
        categorical_features = self.config.get('categorical_features', [])
        encoding_strategy = self.config.get('encoding_strategy', 'onehot')
        
        for feature in categorical_features:
            if feature in df.columns:
                if encoding_strategy == 'onehot':
                    df = pd.get_dummies(df, columns=[feature], prefix=[feature])
                elif encoding_strategy == 'label':
                    df[feature] = df[feature].astype('category').cat.codes
        
        return df