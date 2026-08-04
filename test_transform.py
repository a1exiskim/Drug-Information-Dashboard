from transform import clean_drug_data

# create fake data 

fake_drug = {
    'openfda': {
        'brand_name': ['fake drug'],
        'generic_name': ['fake ingredient'],
        'manufacturer_name': ['fake company']
    },
    'warnings': ['fake warning'],
    'purpose': ['fake purpose'],
    'dosage_and_administration': ['fake dosage and administration'],
    'active_ingredient': ['fake ingredients']
}

def test_brand_name():
    cleaned_drug_data = clean_drug_data(fake_drug)
    assert cleaned_drug_data['drug_name'] == ['fake drug']

def test_generic_name():
    cleaned_drug_data = clean_drug_data(fake_drug)
    assert cleaned_drug_data['generic_name'] == ['fake ingredient']

def test_manufacturer_name():
    cleaned_drug_data = clean_drug_data(fake_drug)
    assert cleaned_drug_data['manufacturer'] == ['fake company']


def test_warnings():
    cleaned_drug_data = clean_drug_data(fake_drug)
    assert cleaned_drug_data['warnings'] == ['fake warning']

def test_purpose():
    cleaned_drug_data = clean_drug_data(fake_drug)
    assert cleaned_drug_data['purpose'] == ['fake purpose']

def test_dosage_and_administration():
    cleaned_drug_data = clean_drug_data(fake_drug)
    assert cleaned_drug_data['dosage_and_administration'] == ['fake dosage and administration']

def test_active_ingredient():
    cleaned_drug_data = clean_drug_data(fake_drug)
    assert cleaned_drug_data['active_ingredient'] == ['fake ingredients']