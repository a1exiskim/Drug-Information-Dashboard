from db import connect_to_db, load_drug
from transform import clean_drug_data
from tests.test_transform import fake_drug_1


def test_load_drug():
    connection = connect_to_db()

    cleaned_drug = clean_drug_data(fake_drug_1)

    load_drug(cleaned_drug, connection)

    connection.close()