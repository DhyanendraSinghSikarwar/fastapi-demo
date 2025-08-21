from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Patient data inserted successfully.")

patient_info = {'name': 'John Doe', 'age': 30}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)

# reusing the pydentic class
def update_patient_data(patient: Patient):
    print("Updating patient data...")
    print(patient.name)
    print(patient.age)
    print("Patient data updated successfully.")

update_patient_data(patient1)