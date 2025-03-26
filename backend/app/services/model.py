from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from app.services import preprocessor

tree = Pipeline(
    steps=[
        ("transformer", preprocessor),
        (
            "DecisionTreeClassifier",
            DecisionTreeClassifier(
                criterion="log_loss",
                splitter="random",
                max_features="auto",
                random_state=42,
            ),
        ),
    ],
    verbose=True,
)

lr = Pipeline(
    steps=[
        ("transformer", preprocessor),
        (
            "LogisticRegression",
            LogisticRegression(
                dual=True, max_iter=1e5, l1_ratio=0.5, n_jobs=-1, random_state=42
            ),
        ),
    ]
)
svc = Pipeline(
    steps=[
        ("transformer", preprocessor),
        ("svc", SVC(kernel="linear", gamma="auto", probability=True, random_state=42)),
    ]
)
mlp = Pipeline(
    steps=[
        ("transformer", preprocessor),
        (
            "MLPClassifier",
            MLPClassifier(
                hidden_layer_sizes=(10, 5),
                activation="relu",
                solver="adam",
                max_iter=500,
                random_state=42,
            ),
        ),
    ]
)
rf = Pipeline(
    steps=[
        ("transformer", preprocessor),
        (
            "RandomForestClassifier",
            RandomForestClassifier(n_estimators=100, random_state=42),
        ),
    ]
)
