from pydantic import (
    BaseModel,
    EmailStr,
    AnyUrl,
    Field,
    model_validator,
    computed_field
)
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

    height: Annotated[
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

    @model_validator(mode="after")
    def validate_emergency_contact(self):
        if self.age is not None and self.age > 60:
            if "emergency" not in self.contact_details:
                raise ValueError(
                    "Emergency contact is required for patients above 60 years old"
                )

        return self

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.diseases)
    print("BMI:", patient.bmi)
    print("inserted into database")


patient_info = {
    "name": "nitish",
    "age": 30,
    "weight": 50,
    "height": 1.70,
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