import axios from "axios";

const apiClient = axios.create({
    baseURL: "http://localhost:8000",
    headers: {
        "Content-Type": "application/json",
    },
});

export default {
    predict(modelName: string, data: any) {
        return apiClient.post("/model/predict", data, {
            params: { model_name: modelName },
        });
    },
};