import requests

response = requests.get('https://api.fda.gov/drug/label.json?search=openfda.brand_name:Tylenol')
data = response.json()

drug = data['results'][0]

# print(drug['openfda']['brand_name'])
# print(drug['openfda']['generic_name'])
# print(drug['openfda']['manufacturer_name'])


print(drug['warnings'][0])