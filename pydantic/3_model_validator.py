from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated

# field validator can be applied on single field, for multiple fields we can use model_validator
# if i apply a validator on age and contact_details fields together, like if age > 60, then we need emergency contact in contact_details . for this we need to use model_validator
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]]
    contact_details: Optional[Dict[str, str]]
    email: EmailStr
    linkedin: AnyUrl

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Emergency contact is required for patients over 60 years old.")
        else:
            return model

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