import category_encoders as ce
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

vectorizer = TfidfVectorizer(
    ngram_range=(1, 3),
    stop_words=[
        "missing",
        "work",
        "job",
        "position",
        "company",
        "qualification",
        "meal",
        "knowledge",
        "establish",
        "degree",
        "require",
        "basic",
    ],
    encoding="utf-8",
    min_df=0.1,
    max_df=0.8,
)

ordinal_encoder = OrdinalEncoder()
scaler = StandardScaler()
count_encoder = ce.CountEncoder()
leave_one_out_encoder = ce.LeaveOneOutEncoder()

preprocessor = ColumnTransformer(
    transformers=[
        ("text_transformer", vectorizer, "text"),
        (
            "OrdinalEncoder",
            ordinal_encoder,
            ["required_education", "required_experience"],
        ),
        (
            "CountEncoder",
            count_encoder,
            ["location", "department", "function"],
        ),
        (
            "LeaveOneOutEncoder",
            leave_one_out_encoder,
            [
                "employment_type",
                "industry",
            ],
        ),
        ("StandScaler", scaler, ["salary", "text_length", "missing"]),
    ],
    remainder="passthrough",
    verbose=True,
)

__all__ = [
    "vectorizer",
    "ordinal_encoder",
    "scaler",
    "frequency_encoder",
    "leave_one_out_encoder",
    "preprocessor",
]
