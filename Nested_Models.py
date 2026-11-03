from pydantic import (
    BaseModel,
    EmailStr,
    AnyUrl,
    Field,
    model_validator,
    computed_field
)

from typing import List, Dict, Optional, Annotated


# -------------------------
# Nested Model
# -------------------------

class Address(BaseModel):
    city: str
    state: str

    pincode: Annotated[
        str,
        Field(pattern=r"^[0-9]{6}$")
    ]

    country: str = "India"


# -------------------------
# Patient Model
# -------------------------

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

    # Nested model
    address: Address

    # Model validator
    @model_validator(mode="after")
    def validate_emergency_contact(self):

        if self.age is not None and self.age > 60:

            if "emergency" not in self.contact_details:
                raise ValueError(
                    "Emergency contact is required for patients above 60 years old"
                )

        return self

    # Computed field
    @computed_field
    @property
    def bmi(self) -> float:

        return round(
            self.weight / (self.height ** 2),
            2
        )


# -------------------------
# Function
# -------------------------

def insert_patient_data(patient: Patient):

    print("Name:", patient.name)
    print("Age:", patient.age)
    print("Diseases:", patient.diseases)

    print("City:", patient.address.city)
    print("State:", patient.address.state)
    print("Pincode:", patient.address.pincode)

    print("BMI:", patient.bmi)

    print("Inserted into database")


# -------------------------
# Patient Data
# -------------------------

patient_info = {

    "name": "nitish",
    "age": 30,

    "weight": 50,
    "height": 1.70,

    "yt_url": "https://youtube.com/1322",

    "email": "abc123@hdfc.com",

    "diseases": [
        "flu",
        "cold"
    ],

    "allergies": [
        "pollen",
        "dust"
    ],

    "contact_details": {
        "email": "aabc@gmail.com",
        "phone": "2345"
    },

    # Nested Address
    "address": {
        "city": "Meerut",
        "state": "Uttar Pradesh",
        "pincode": "250001"
    }
}


patient = Patient(**patient_info)

insert_patient_data(patient)


# second way to create nested model
from pydantic import BaseModel
from typing import Optional


class Address(BaseModel):
    city: str
    state: str
    pincode: str
    country: str = "India"


class Patient(BaseModel):
    name: str
    age: Optional[int] = None
    address: Address


# Step 1: Create Address object
address_info = Address(
    city="Meerut",
    state="Uttar Pradesh",
    pincode="250001"
)


# Step 2: Pass Address object to Patient
patient = Patient(
    name="Nitish",
    age=30,
    address=address_info
)


print(patient)