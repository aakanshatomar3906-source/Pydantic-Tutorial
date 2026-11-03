# In Pydantic, serialization means converting your Pydantic model into formats that are easy to store or send, mainly:

# Python dictionary → model_dump()
# JSON string → model_dump_json()

# 1. Python dictionary
# patient_dict = patient.model_dump()

# print(patient_dict)
# print(type(patient_dict))

# Output will look like:

# {
#     'name': 'nitish',
#     'age': 30,
#     'weight': 50.0,
#     'height': 1.7,
#     'yt_url': AnyUrl('https://youtube.com/1322'),
#     'email': 'abc123@hdfc.com',
#     'diseases': ['flu', 'cold'],
#     'allergies': ['pollen', 'dust'],
#     'contact_details': {
#         'email': 'aabc@gmail.com',
#         'phone': '2345'
#     },
#     'address': {
#         'city': 'Meerut',
#         'state': 'Uttar Pradesh',
#         'pincode': '250001',
#         'country': 'India'
#     },
#     'bmi': 17.3
# }

# So:

# patient.model_dump()

# means:

# Pydantic Model → Python Dictionary



# 2. JSON

# For JSON, use:

# patient_json = patient.model_dump_json()

# print(patient_json)
# print(type(patient_json))

# Output:

# {"name":"nitish","age":30,"weight":50.0,"height":1.7,"yt_url":"https://youtube.com/1322","email":"abc123@hdfc.com","diseases":["flu","cold"],"allergies":["pollen","dust"],"contact_details":{"email":"aabc@gmail.com","phone":"2345"},"address":{"city":"Meerut","state":"Uttar Pradesh","pincode":"250001","country":"India"},"bmi":17.3}

# And:

# type(patient_json)

# gives:

# <class 'str'>

# Because JSON is represented as a string in Python


# 3. Pretty JSON

# You can make it easier to read:

# print(patient.model_dump_json(indent=4))

# Output:

# {
#     "name": "nitish",
#     "age": 30,
#     "weight": 50.0,
#     "height": 1.7,
#     "yt_url": "https://youtube.com/1322",
#     "email": "abc123@hdfc.com",
#     "diseases": [
#         "flu",
#         "cold"
#     ],
#     "allergies": [
#         "pollen",
#         "dust"
#     ],
#     "contact_details": {
#         "email": "aabc@gmail.com",
#         "phone": "2345"
#     },
#     "address": {
#         "city": "Meerut",
#         "state": "Uttar Pradesh",
#         "pincode": "250001",
#         "country": "India"
#     },
#     "bmi": 17.3
# }



# 4. Save JSON into a .json file

# If you specifically want a JSON file:

# with open("patient.json", "w") as f:
#     f.write(patient.model_dump_json(indent=4))

# Pydantic Model
#       │
#       ├── model_dump()
#       │        ↓
#       │   Python Dictionary
#       │
#       └── model_dump_json()
#                ↓
#           JSON String
#                ↓
#           .json file


# And the reverse operation is deserialization:

# Python Dictionary / JSON
#           ↓
#     Patient(**data)
#           ↓
#     Pydantic Model


# 1. include — only keep selected fields

# Suppose you only want name, age, and weight:

# data = patient.model_dump(
#     include={"name", "age", "weight"}
# )

# print(data)

# Output:

# {
#     "name": "nitish",
#     "age": 30,
#     "weight": 50.0
# }

# Think:

# include = "I only want these fields."

# 2. exclude — remove selected fields

# Suppose you want everything except email and contact_details:

# data = patient.model_dump(
#     exclude={"email", "contact_details"}
# )

# print(data)

# Output:

# {
#     "name": "nitish",
#     "age": 30,
#     "weight": 50.0,
#     "height": 1.7,
#     "yt_url": "...",
#     "diseases": ["flu", "cold"],
#     "allergies": ["pollen", "dust"],
#     "address": {...},
#     "bmi": 17.3
# }

# Think:

# exclude = "Give me everything except these fields."

# 3. include with nested models

# This is particularly useful with your Address nested model.

# Your structure is:

# Patient
# │
# ├── name
# ├── age
# ├── weight
# ├── email
# └── address
#      ├── city
#      ├── state
#      ├── pincode
#      └── country

# Suppose you want only the patient's name and city + state:

# data = patient.model_dump(
#     include={
#         "name",
#         "address": {"city", "state"}
#     }
# )

# print(data)

# Output:

# {
#     "name": "nitish",
#     "address": {
#         "city": "Meerut",
#         "state": "Uttar Pradesh"
#     }
# }

# This is called nested include.

# 4. exclude with nested models

# Suppose you want the complete patient data but don't want the pincode:

# data = patient.model_dump(
#     exclude={
#         "address": {"pincode"}
#     }
# )

# Then:

# "address": {
#     "city": "Meerut",
#     "state": "Uttar Pradesh",
#     "country": "India"
# }

# The pincode is removed.

# 5. include vs exclude
# 	include	exclude
# Purpose	Select what to keep	Select what to remove
# Example	{"name", "age"}	{"email"}
# Output	Only selected fields	Everything except selected fields
# Best when	You need a small specific response	You need almost everything
# Easy memory trick
# include → KEEP these
# exclude → REMOVE these
# 6. Serialization to JSON

# The same concept works with model_dump_json():

# json_data = patient.model_dump_json(
#     include={"name", "age", "address"}
# )

# print(json_data)

# And:

# json_data = patient.model_dump_json(
#     exclude={"email", "contact_details"}
# )
# 7. A practical API example

# This is where include/exclude becomes really useful.

# Imagine your backend has a patient object containing:

# name
# age
# weight
# email
# contact_details
# address
# diseases

# For a public API response, you might want:

# patient.model_dump(
#     exclude={
#         "email",
#         "contact_details"
#     }
# )

# But for a doctor's dashboard, you might include more information:

# patient.model_dump()

# And for a basic patient list, you might only send:

# patient.model_dump(
#     include={
#         "name",
#         "age",
#         "diseases"
#     }
# )

# So include and exclude are basically filters applied during serialization.

# One-line concept
# Pydantic Model
#       ↓
#  model_dump(include / exclude)
#       ↓
# Selected Dictionary
#       ↓
# JSON / API Response