import pandas as pd
from fastapi import APIRouter, Query, Request

from app.schemas import SuccessResponseSchema
from app.services.data_transformer import data_loader
from app.services.model_loader import get_model

router = APIRouter(prefix="/model", tags=["模型接口"])


@router.api_route(
    "/predict",
    methods=["POST"],
    tags=["模型接口"],
    response_description="使用模型进行预测",
    response_model=SuccessResponseSchema,
)
async def predict(
    request: Request, model_name: str = Query("stacking", description="模型名称")
):
    model = get_model(model_name)
    json_data = await request.json()
    # pred = int(model.predict(json_data)[0])
    data = data_loader(json_data)
    proba = model.predict_proba(pd.DataFrame([data]))[0]
    return SuccessResponseSchema(
        data={
            "probability": {
                "label_0": float(proba[0]),
                "label_1": float(proba[1]),
            }
        }
    )
