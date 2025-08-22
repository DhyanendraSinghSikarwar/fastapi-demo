from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Annotated
import json

app = FastAPI()

class Patient(BaseModel):

    id: Annotated[str, Field(..., description="ID of the patient", examples=['P001'])]
    name: Annotated[str, Field(..., description="Name of the patient", examples=['John Doe'])]
    city: Annotated[str, Field(..., description="City where the patient is living", examples=['New York'])]
    age: Annotated[int, Field(..., description="Age of the patient", examples=[30])]
    gender: Annotated[str, Field(..., description="Gender of the patient", examples=['Male'])]
    height: Annotated[float, Field(..., description="Height of the patient in meters", examples=[1.75])]
    weight: Annotated[float, Field(..., description="Weight of the patient in kilograms", examples=[70.0])]

def load_data():
    with open("patients.json") as f:
        return json.load(f)

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