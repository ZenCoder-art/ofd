import joblib
import pandas as pd
from app.schemas import SuccessResponseSchema
from app.schemas.predict_schema import ModelName, PredictionRequest
from fastapi import APIRouter, Query

router = APIRouter(prefix="/model", tags=["模型接口"])

models = {
    "DecisionTreeClassifier": joblib.load("./app/models/DecisionTreeClassifier.joblib"),
    "LogisticRegression": joblib.load("./app/models/LogisticRegression.joblib"),
    "LinearSVC": joblib.load("./app/models/LinearSVC.joblib"),
    "RandomForestClassifier": joblib.load("./app/models/RandomForestClassifier.joblib"),
    "SGDClassifier": joblib.load("./app/models/SGDClassifier.joblib"),
}


# @router.api_route(
#     "/all-predict",
#     methods=["POST"],
#     summary="获取所有模型的预测结果",
#     response_model=SuccessResponseSchema,
# )
# async def all_predict(request: PredictionRequest):
#     try:
#         input_data = preprocess_data(request)
#         results = {}
#         for model_name, model in models.items():
#             try:
#                 prediction = model.predict(input_data)
#                 proba = model.predict_proba(input_data)
#                 results[model_name] = {
#                     "predict": int(prediction[0]),
#                     "probabilities": {
#                         "class_0": float(proba[0][0]),
#                         "class_1": float(proba[0][1]),
#                     },
#                 }
#             except Exception as e:
#                 results[model_name] = {"error": str(e)}

#         return SuccessResponseSchema(data=results)

#     except Exception as e:
#         raise e


@router.api_route(
    "/predict",
    methods=["POST"],
    summary="使用单一模型进行预测",
    response_model=SuccessResponseSchema,
)
async def predict(
    model_name: ModelName = Query(..., description="使用的模型名称"),
    request: PredictionRequest = Query(
        default={
            "title": "Senior Data Scientist",
            "description": "We are looking for a data scientist...",
            "requirements": "Master's degree in Computer Science...",
            "company_profile": "A leading tech company...",
            "benefits": "Health insurance, paid vacation...",
            "salary": 120000,
            "required_education": "bachelor and above",
            "required_experience": "3-5 years",
            "location": "New York",
            "department": "Data Science",
            "function": "Research and Development",
            "employment_type": "Full-time",
            "industry": "Technology",
            "missing": 0,
        },
        description="请求参数",
    ),
):
    try:
        input_data = pd.DataFrame([request.model_dump()])
        text_columns = [
            "title",
            "description",
            "requirements",
            "company_profile",
            "benefits",
        ]
        input_data["text"] = (
            input_data[text_columns]
            .fillna("")
            .astype(str)
            .agg(lambda x: " ".join(x.str.strip()), axis=1)
            .str.replace(r"\s+", " ", regex=True)
        )
        input_data["text_length"] = input_data["text"].apply(len)
        input_data = input_data.drop(columns=text_columns)
        model = models[model_name]
        prediction = model.predict(input_data)
        probabilities = model.predict_proba(input_data)
        return SuccessResponseSchema(
            data={
                "predict": int(prediction[0]),
                "predict_prob_class_1": float(probabilities[0][1]),
                "predict_prob_class_0": float(probabilities[0][0]),
            }
        )
    except Exception as e:
        raise e


@router.api_route(
    "/models",
    methods=["GET"],
    summary="获取当前可用的所有模型",
    response_model=SuccessResponseSchema,
)
async def get_models():
    """返回所有可用模型的名称及其参数"""
    try:
        return SuccessResponseSchema(data=list(models.keys()))
    except Exception as e:
        raise e
