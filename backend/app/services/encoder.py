import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class OrdinalEncoder(BaseEstimator, TransformerMixin):
    def __init__(self) -> None:
        self.mappings = {}

    def fit(self, X, y=None):
        for idx in range(X.shape[1]):
            unique = np.unique(X[:, idx])
            mapping = {val: idx for idx, val in enumerate(unique)}
            self.mappings[idx] = mapping
        return self

    def transform(self, X):
        X_transformed = np.zeros(X.shape, dtype=int)
        for idx in range(X.shape[1]):
            mapping = self.mappings[idx]
            X_transformed[:, idx] = [mapping[val] for val in X[:, idx]]
        return X_transformed

    def inverse_transform(self, X):
        X_inverse = np.zeros(X.shape, dtype=object)
        for idx in range(X.shape[1]):
            mapping = self.mappings[idx]
            inverse_mapping = {idx: val for val, idx in mapping.items()}
            X_inverse[:, idx] = [inverse_mapping[val] for val in X[:, idx]]
        return X_inverse


class FrequencyEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, handle_unknown: str = "unknown") -> None:
        self.mappings = {}
        self.handle_unknown = handle_unknown

    def fit(self, X, y=None):
        for idx in range(X.shape[1]):
            unique, counts = np.unique(X[:, idx], return_counts=True)
            frequency = counts / counts.sum()
            mapping = {val: freq for val, freq in zip(unique, frequency)}
            self.mappings[idx] = mapping
        return self

    def transform(self, X):
        X_transformed = np.zeros(X.shape, dtype=float)
        for idx in range(X.shape[1]):
            mapping = self.mappings[idx]
            if self.handle_unknown == "unknown":
                X_transformed[:, idx] = np.array(
                    [mapping.get(val, 0) for val in X[:, idx]]
                )
            else:
                X_transformed[:, idx] = np.array(
                    [mapping.get(val, np.nan) for val in X[:, idx]]
                )
            return X_transformed

    def inverse_transform(self, X):
        X_inverse = np.zeros(X.shape, dtype=object)
        for idx in range(X.shape[1]):
            mapping = self.mappings[idx]
            inverse_mapping = {idx: val for val, idx in mapping.items()}
            X_inverse[:, idx] = np.array(
                [inverse_mapping.get(val, "unknown") for val in X[:, idx]]
            )
        return X_inverse


if __name__ == "__main__":
    pass
