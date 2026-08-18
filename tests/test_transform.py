import pytest
from transform import clean_drug_data

# --- create fake data ---

fake_drug_1 = {
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

# missing brand_name key
fake_drug_2 = {
    'openfda': {
        'generic_name': ['fake ingredient'],
        'manufacturer_name': ['fake company']
    },
    'warnings': ['fake warning'],
    'purpose': ['fake purpose'],
    'dosage_and_administration': ['fake dosage and administration'],
    'active_ingredient': ['fake ingredients']
    }

# missing manufacturer_name key and multivalue defauls
fake_drug_3 = {
    'openfda': {
            'brand_name': ['fake drug'],
            'generic_name': ['fake ingredient']
    }
    }

# empty keys
fake_drug_4 = {
    'openfda': {
            'brand_name': ['fake drug'],
            'generic_name': ['fake ingredient'],
            'manufacturer_name': ['fake company']
        },
        'warnings': ['fake warning'],
        'purpose': ['fake purpose'],
        'dosage_and_administration': ['fake dosage and administration'],
        'active_ingredient': []
}

# --- test cases ---

def test_brand_name():
    cleaned_drug_data = clean_drug_data(fake_drug_1)
    assert cleaned_drug_data['drug_name'] == 'fake drug'

def test_generic_name():
    cleaned_drug_data = clean_drug_data(fake_drug_1)
    assert cleaned_drug_data['generic_name'] == 'fake ingredient'

def test_manufacturer_name():
    cleaned_drug_data = clean_drug_data(fake_drug_1)
    assert cleaned_drug_data['manufacturer'] == 'fake company'

def test_warnings():
    cleaned_drug_data = clean_drug_data(fake_drug_1)
    assert cleaned_drug_data['warnings'] == 'fake warning'

def test_purpose():
    cleaned_drug_data = clean_drug_data(fake_drug_1)
    assert cleaned_drug_data['purpose'] == 'fake purpose'

def test_dosage_and_administration():
    cleaned_drug_data = clean_drug_data(fake_drug_1)
    assert cleaned_drug_data['dosage_and_administration'] == 'fake dosage and administration'

def test_active_ingredient():
    cleaned_drug_data = clean_drug_data(fake_drug_1)
    assert cleaned_drug_data['active_ingredient'] == 'fake ingredients'

def test_empty_brand_name():
    with pytest.raises(KeyError):
        cleaned_drug_data = clean_drug_data(fake_drug_2)

def test_missing_keys():
    cleaned_drug_data = clean_drug_data(fake_drug_3)
    assert cleaned_drug_data['manufacturer'] == 'No information available'
    assert cleaned_drug_data['warnings'] == 'No information available'
    assert cleaned_drug_data['purpose'] == 'No information available'
    assert cleaned_drug_data['dosage_and_administration'] == 'No information available'
    assert cleaned_drug_data['active_ingredient'] == 'No information available'

def test_empty_keys():
    cleaned_drug_data = clean_drug_data(fake_drug_4)
    assert cleaned_drug_data['active_ingredient'] == 'No information available'