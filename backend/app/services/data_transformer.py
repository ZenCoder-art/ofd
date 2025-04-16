def data_loader(data: dict) -> dict:
    fields = ["title", "description", "requirements", "company_profile", "benefits"]
    required_fields = [
        "function",
        "location",
        "department",
        "industry",
        "employment_type",
        "salary",
        "required_education",
        "required_experience",
    ]
    text = " ".join([data.get(field, "") for field in fields if data.get(field)])
    text_length = len(text)
    extra_info = {"text": text, "text_length": text_length}
    for field in fields:
        data.pop(field, None)
    for field in required_fields:
        if field == "salary":
            data.setdefault(field, 0)
        data.setdefault(field, "")
    data.update(extra_info)
    return data


if __name__ == "__main__":
    data = {
        "title": "Software Engineer",
        "description": "We are hiring Python developers.",
        "requirements": "Experience with FastAPI",
        "company_profile": "An innovative tech company",
        "employment_type": "",
        "function": "",
        "location": "",
        "department": "",
        "industry": "",
        "salary": "",
        "required_education": "",
        "required_experience": "",
        "benefits": "",
    }
    print(data_loader(data))
