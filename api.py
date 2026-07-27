import requests

def get_drug_data(drug_name):
    url = f'https://api.fda.gov/drug/label.json?search=openfda.brand_name:{drug_name}'

    response = requests.get(url)
    data = response.json()

    return data

