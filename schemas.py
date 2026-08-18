from pydantic import BaseModel


class DrugResponse(BaseModel):
    drug_name: str
    generic_name: str
    manufacturer: str
    purpose: str
    warnings: str
    dosage_and_administration: str
    active_ingredient: str