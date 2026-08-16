from db import get_drug, load_drug
from transform import clean_drug_data
from api import get_drug_data

def find_or_fetch_drug(drug_name, connection):
    '''look for drug in database, if it does not exist, source from API and add to database'''
    
    drug_result = get_drug(drug_name, connection)

    if drug_result is not None:
        return drug_result
    else:
        raw_drug_data = get_drug_data(drug_name)
        drug = clean_drug_data(raw_drug_data)
        load_drug(drug, connection)

        return drug