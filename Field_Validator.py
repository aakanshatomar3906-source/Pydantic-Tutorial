from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: Annotated[
        str,
        Field(
            max_length=50,
            title="Name of the patient",
            description="This is the name of the patient",
            examples=["Nitish", "Amit"]
        )
    ]

    age: Optional[int] = None

    weight: Annotated[
        float,
        Field(gt=0, strict=True)
    ]

    yt_url: AnyUrl
    email: EmailStr
    diseases: List[str]

    allergies: Annotated[
        Optional[List[str]],
        Field(default=None, max_length=20)
    ]

    contact_details: Dict[str, str]

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        valid_domains = ["hdfc.com", "icici.com"]
        domain_name = value.split("@")[-1]

        if domain_name not in valid_domains:
            raise ValueError(
                "email domain should be hdfc.com or icici.com"
            )

        return value

    @field_validator("name")
    @classmethod
    def name_validator(cls, name):
        return name.upper()

    @field_validator("age", mode="before")
    @classmethod
    def age_validator(cls, value):
        if value is None:
            return value

        if 0 < value < 100:
            return value
        else:
            raise ValueError("age should be between 0 and 100")


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.diseases)
    print("inserted into database")


patient_info = {
    "name": "nitish",
    "age": 30,
    "weight": 50,
    "yt_url": "https://youtube.com/1322",
    "email": "abc123@hdfc.com",
    "diseases": ["flu", "cold"],
    "allergies": ["pollen", "dust"],
    "contact_details": {
        "email": "aabc@gmail.com",
        "phone": "2345"
    }
}

patient = Patient(**patient_info)

insert_patient_data(patient)