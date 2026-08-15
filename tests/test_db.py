from db import connect_to_db, load_drug
from db import get_drug
from transform import clean_drug_data
from tests.test_transform import fake_drug_1


def test_loading_drug():
    connection = connect_to_db()

    cleaned_drug = clean_drug_data(fake_drug_1)

    load_drug(cleaned_drug, connection)

    connection.close()


def test_get_drug():
    connection = connect_to_db()

    clean_drug = clean_drug_data(fake_drug_1)

    load_drug(clean_drug, connection)

    fake_drug_row = get_drug('fake drug', connection)
    assert fake_drug_row['drug_name'] == 'fake drug'
    assert fake_drug_row['warnings'] == ['fake warning']


def test_get_drug_not_found():
    connection = connect_to_db()

    empty_drug_row = get_drug('ur mom', connection)
    assert empty_drug_row is None
