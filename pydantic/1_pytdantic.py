from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


# by default all fields are required, but we can make them optional using Optional[]
# Field is used for custom validations
# by using Anotation and Field, we can add title, descriptions, etc to improve visibilty (attach meta data) for the user
class Patient(BaseModel):
    name: Annotated[str, Field(..., min_length=2, max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 charaters', examples=['Dhyanendra', 'John'])]  # name must be between 2 and 50 characters
    age: int = Field(gt=0, lt=120)                        # age must be between 0 and 120
    weight: Annotated[float, Field(gt=0, strict= True)]   # weight must be greater than 0. Also strict will not convert any datatype like from string to float, by doing strict True, it will throw an error if data type is other than float
    married: Annotated[bool,Field(default=False, description='Is the patient married or not')]                            # Annoted field with default value False with description 
    allergies: Optional[List[str]] = Field(max_length=5)  # max 5 allergies allowed
                                                          # allergies is a list and inside this all items will be string that will also be validated
                                                          # if we use 'list' then it will validate inside items' datatypes
                                                          # if we use 'Optional' then the whole list can be None, we have to add default value to Optional parameter
    contact_details: Optional[Dict[str, str]] = {}        # Optional field with default empty dict
    email: EmailStr
    linkedin: AnyUrl

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.email)
    print("Patient data inserted successfully.")

patient_info = {'name': 'John Doe', 'age': 30, 'weight': 70.5, 'married': True, 'allergies': ['penicillin'], 'contact_details': {'phone': '123-456-7890'}, 'email': 'john.doe@example.com', 'linkedin': 'https://www.linkedin.com/in/johndoe'}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)

# reusing the pydentic class
def update_patient_data(patient: Patient):
    print("Updating patient data...")
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.email)
    print(patient.linkedin)
    print("Patient data updated successfully.")

update_patient_data(patient1)