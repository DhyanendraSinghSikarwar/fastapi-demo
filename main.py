from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json

app = FastAPI()

class Patient(BaseModel):

    id: Annotated[str, Field(..., description="ID of the patient", examples=['P001'])]
    name: Annotated[str, Field(..., description="Name of the patient", examples=['John Doe'])]
    city: Annotated[str, Field(..., description="City where the patient is living", examples=['New York'])]
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the patient", examples=[30])]
    gender: Annotated[Literal['male', 'female', 'other'], Field(..., description="Gender of the patient", examples=['male'])]
    height: Annotated[float, Field(..., gt=0, description="Height of the patient in meters", examples=[1.75])]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the patient in kilograms", examples=[70.0])]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 24.9:
            return "Normal weight"
        elif 25 <= self.bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field( default=None)]
    city: Annotated[Optional[str], Field( default=None)]
    age: Annotated[Optional[int], Field( gt=0, lt=120, default=None)]
    gender: Annotated[Optional[Literal['male', 'female', 'other']], Field( default=None)]
    height: Annotated[Optional[float], Field( gt=0, default=None)]
    weight: Annotated[Optional[float], Field( gt=0, default=None)]

def load_data():
    with open("patients.json") as f:
        return json.load(f)

def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f, default=str)

@app.get("/")
def hello():
    return {"message": "Patient Management System API"}

@app.get("/about")
def about():
    return {"message": "A fully functional API for managing patient data."}
    
@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description="Sort on the basis of height, weight or bmi")):
    data = load_data()
    # import pdb; pdb.set_trace()  # Debugging line to inspect the patient_id
    print(patient_id)
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="Sort on the basis of height, weight or bmi"), order: str = Query("asc", description="sort in asc or desc order")):
    valid_fields = ["height", "weight", "bmi"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field, select from {valid_fields}")
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order, use 'asc' or 'desc'")
    
    data = load_data()
    sort_order = True if order == "desc" else False
    
    sorted_data = dict(sorted(data.items(), key=lambda item: item[1].get(sort_by, ""), reverse=sort_order))
    return sorted_data

@app.post("/create")
def create_patient(patient: Patient):
    # load the data
    data = load_data()

    # check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")
    # add new patient to the data but patient is pydantic object and needs to be converted to dict
    data[patient.id] = patient.model_dump(exclude=["id"])  # this will also include computed fields

    # save the data
    save_data(data)

    return JSONResponse(status_code=201, content={"message": "Patient created successfully"})

@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):

    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    # Update patient data
    existing_patient_info = data[patient_id]                               # fetch the existing patient info
    updated_patient_info = patient_update.model_dump(exclude_unset=True)   # fetch the updated patient info with only updated field using exclude_unset =True

    for key, value in updated_patient_info.items():                        # Now, we have update the existing patient info with the new values
        existing_patient_info[key] = value

    # Now, Since we do have updated value of BMI and verdict so, we have to convert the updated existing_patient_info into patient pytantic model
    existing_patient_info['id'] = patient_id
    existing_patient_info = Patient(**existing_patient_info) # while converting, it required "id" field as well, so we have add it

    # convert from pydantic model to dict
    existing_patient_info = existing_patient_info.model_dump(exclude=["id"])  # here, again we need to remove the "id" column, before adding into dictionary (since it is not present in values)

    # add this dict to our data
    data[patient_id] = existing_patient_info

    # save data
    save_data(data)

    return JSONResponse(status_code=200, content={"message": "Patient updated successfully"})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    del data[patient_id]
    save_data(data)

    return JSONResponse(status_code=200, content={"message": "Patient deleted successfully"})