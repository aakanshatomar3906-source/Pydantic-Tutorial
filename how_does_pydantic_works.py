# How does Pydantic works?
# 1. define a pydantic Model
# 2. instantiate the model with some data( raw)
# 3. validate the data using the model

# to check the versin : python -c "import pydantic; print(pydantic.__version__)"

# from pydantic import BaseModel

# class Patient(BaseModel):
#     name: str
#     age: int

# def insert_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print('inserted into database')

# patient_info={'name':'nitish','age':'thirty'}
# patient=Patient(**patient_info)


# TYPE VALIDATION
# from pydantic import BaseModel
# from typing import List,Dict,Optional

# class Patient(BaseModel):
#     name: str
#     age:Optional[ int] = None
#     diseases: List[str]
#     allergies: Optional[List[str]] = None
#     contact_details: Dict[str,str]


# def insert_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print(patient.diseases)
#     print('inserted into database')

# patient_info={'name':'nitish','age':30,'diseases':['flu','cold'],"allergies":["pollen","dust"],'contact_details':{'email':'aabc@gmail.com','phone':'2345'}}
# patient=Patient(**patient_info)


# DATA VALIDATION
# one way
# from pydantic import BaseModel,EmailStr,AnyUrl
# from typing import List,Dict,Optional

# class Patient(BaseModel):
#     name: str
#     age:Optional[ int] = None
#     yt_url:AnyUrl
#     email:EmailStr
#     diseases: List[str]
#     allergies: Optional[List[str]] = None
#     contact_details: Dict[str,str]


# def insert_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print(patient.diseases)
#     print('inserted into database')

# patient_info={'name':'nitish','age':30,'yt_url':'youtube.com/1322','email':'abc123','diseases':['flu','cold'],"allergies":["pollen","dust"],'contact_details':{'email':'aabc@gmail.com','phone':'2345'}}
# patient=Patient(**patient_info)


# second way
from pydantic import BaseModel, EmailStr, AnyUrl, Field
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