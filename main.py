from fastapi import FastAPI, HTTPException 
from db import connect_to_db
from pipeline import find_or_fetch_drug

app = FastAPI()

@app.get("/drugs/{drug_name}")
def get_drug_endpoint(drug_name: str):
    connection = connect_to_db()
    obtained = find_or_fetch_drug(drug_name, connection)

    if obtained is None:
        raise HTTPException(status_code=404, detail="Drug not found")

    return obtained
