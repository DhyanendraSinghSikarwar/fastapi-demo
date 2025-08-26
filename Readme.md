# Patient Management System API

A FastAPI-based RESTful API for managing patient data, including creation, retrieval, updating, deletion, and sorting of patient records. This project demonstrates the use of FastAPI, Pydantic models, and JSON-based data storage.

## Features

- Add new patients with detailed information
- View all patients or a specific patient by ID
- Update patient details
- Delete patient records
- Sort patients by height, weight, or BMI
- Computed fields for BMI and health verdict

## Endpoints

| Method | Endpoint                | Description                                 |
|--------|-------------------------|---------------------------------------------|
| GET    | `/`                     | Welcome message                             |
| GET    | `/about`                | API description                             |
| GET    | `/view`                 | View all patients                           |
| GET    | `/patient/{patient_id}` | View a specific patient by ID               |
| GET    | `/sort`                 | Sort patients by height, weight, or BMI     |
| POST   | `/create`               | Add a new patient                           |
| PUT    | `/edit/{patient_id}`    | Update an existing patient                  |
| DELETE | `/delete/{patient_id}`  | Delete a patient                            |

## Data Model

Each patient record includes:
- `id`: Patient ID (string)
- `name`: Name (string)
- `city`: City (string)
- `age`: Age (integer)
- `gender`: Gender (male, female, or other)
- `height`: Height in meters (float)
- `weight`: Weight in kilograms (float)
- `bmi`: Computed Body Mass Index (float)
- `verdict`: Health verdict based on BMI (string)

## Getting Started

### Prerequisites
- Python 3.8+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)

- [Streamlit](https://streamlit.io/) (for the frontend)

### Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd fastapi-demo
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install streamlit
   ```

### Running the API
Start the server with:
```bash
uvicorn main:app --reload
```
The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Running the Streamlit Frontend
Start the Streamlit app with:
```bash
streamlit run frontend.py
```
The frontend will open in your browser (usually at [http://localhost:8501](http://localhost:8501)).

### API Documentation
Interactive docs are available at:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Data Storage
Patient data is stored in a local `patients.json` file. Ensure this file is present in the project directory.

## License
This project is for educational purposes.
