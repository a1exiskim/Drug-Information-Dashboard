import requests
from requests.exceptions import HTTPError

def get_drug_data(drug_name):
    url = f'https://api.fda.gov/drug/label.json?search=openfda.brand_name:{drug_name}'

    response = requests.get(url, timeout=10)    
    try:
        response.raise_for_status()
    except HTTPError:
        if response.status_code == 404:
            return None
        raise 
    
    data = response.json()
    result = data.get('results')

    if result:
        return result[0]

    return None 
