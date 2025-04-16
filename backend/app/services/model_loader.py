from functools import lru_cache

import joblib


@lru_cache()
def get_model(name: str):
    if name == "lr":
        return joblib.load("app/models/base-models/LogisticRegression.joblib")
    elif name == "rf":
        return joblib.load("app/models/base-models/RandomForestClassifier.joblib")
    elif name == "dt":
        return joblib.load("app/models/base-models/DecisionTreeClassifier.joblib")
    else:
        return joblib.load("app/models/fusion-models/m8.joblib")