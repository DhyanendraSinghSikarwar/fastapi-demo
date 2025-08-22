from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

# i want to apply field validators to email value. i want to check where are user from icici and hdfc bank or not

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]]
    contact_details: Optional[Dict[str, str]]
    email: EmailStr
    linkedin: AnyUrl

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['icici.com', 'hdfc.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("Email must be from ICICI or HDFC bank.")
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()


    # mode is before/after , it means when the validation should be applied before or after the datatype conversion
    @field_validator('age', mode='after') # default value of mode is after
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        raise ValueError("Age must be a positive integer between 1 and 99.")

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

patient_info = {'name': 'John Doe', 'age': '30', 'weight': 70.5, 'married': True, 'allergies': ['penicillin'], 'contact_details': {'phone': '123-456-7890'}, 'email': 'john.doe@hdfc.com', 'linkedin': 'https://www.linkedin.com/in/johndoe'}

patient1 = Patient(**patient_info)

update_patient_data(patient1)