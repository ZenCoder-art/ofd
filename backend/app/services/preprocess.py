from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer


class PreProcessor:
    def __init__(self) -> None:
        self.preprocessor = ColumnTransformer(
            transformers=[
                ("text_transformer", text_transformer, "text"),
                ("OrdinalEncoder", ordinal_encoder, ordinal_columns),
                ("FrequencyEncoder", frequency_encoder, frequency_columns),
                ("LeaveOneOutEncoder", leave_one_out_encoder, leave_one_out_columns),
                ("StandScaler", scaler, num_columns),
            ],
            remainder="passthrough",
            verbose=True,
        )

    def feature_construction(self, dataset):
        # 构造一个字段用于统计某个样本含有缺失值字段的个数
        columns = [col for col in dataset.columns if col.startswith("is_missing")]
        dataset["missing"] = dataset[columns].sum(axis=1)
        dataset = dataset.drop(columns=columns)
        # 将长文本型变量合并为一个变量
        dataset["text"] = (
            dataset["title"]
            + " "
            + dataset["description"]
            + " "
            + dataset["requirements"]
            + " "
            + dataset["company_profile"]
            + " "
            + dataset["benefits"]
        )
        dataset = dataset.drop(
            columns=[
                "title",
                "description",
                "requirements",
                "company_profile",
                "benefits",
            ]
        )
        # 统计文本长度
        dataset["text_length"] = dataset["text"].apply(len)
        return dataset

    def feature_transformer(self):
        ...
