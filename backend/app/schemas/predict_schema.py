from enum import Enum

from pydantic import BaseModel


class ModelName(str, Enum):
    TREE = "DecisionTreeClassifier"
    LOGISTIC_REGRESSION = "LogisticRegression"
    LSVC = "LinearSVC"
    RANDOM_FOREST = "RandomForestClassifier"
    SGDC = "SGDClassifier"


class PredictionRequest(BaseModel):
    title: str
    description: str
    requirements: str
    company_profile: str
    benefits: str
    salary: float
    required_education: str
    required_experience: str
    location: str
    department: str
    function: str
    employment_type: str
    industry: str
    missing: int

    class Config:
        json_schema_extra = {
            "example": {
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
            }
        }
