from pydantic import BaseModel, EmailStr, AnyUrl, computed_field
from typing import List, Dict, Optional

# on the go (dynamically) computed fields (calculated from other fields) example calculating BMI from weight and height values
class Patient(BaseModel):
    name: str
    age: int
    weight: float  # kg
    height: float  # mtr
    married: bool
    allergies: Optional[List[str]]
    contact_details: Optional[Dict[str, str]]
    email: EmailStr
    linkedin: AnyUrl

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi

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
    print("Calculated BMI:", patient.bmi)    # function name become property of calculated field
    print("Patient data updated successfully.")

patient_info = {'name': 'John Doe', 'age': '30', 'weight': 75.2, 'height': 1.75, 'married': True, 'allergies': ['penicillin'], 'contact_details': {'phone': '123-456-7890'}, 'email': 'john.doe@hdfc.com', 'linkedin': 'https://www.linkedin.com/in/johndoe'}

patient1 = Patient(**patient_info)

update_patient_data(patient1)