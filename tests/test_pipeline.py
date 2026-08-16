from db import connect_to_db, load_drug
from .test_transform import fake_drug_1
from transform import clean_drug_data
from pipeline import find_or_fetch_drug
from psycopg.rows import dict_row
from unittest.mock import patch

def test_drug_in_database():
    connection = connect_to_db()
    cursor = connection.cursor(row_factory=dict_row)

    cleaned_drug = clean_drug_data(fake_drug_1)

    load_drug(cleaned_drug, connection)

    # patch pipeline calling API 
    with patch('pipeline.get_drug_data') as mock_api:
        found_drug = find_or_fetch_drug('fake drug', connection)
        assert mock_api.called == False

    assert found_drug['drug_name'] == 'fake drug'

    cursor.execute('DELETE FROM drugs WHERE drug_name = %s',
                   ('fake drug',))

    connection.commit()
    cursor.close()
    connection.close()

def test_drug_not_in_database():
    connection = connect_to_db()
    cursor = connection.cursor(row_factory=dict_row)

    with patch('pipeline.get_drug_data') as mock_api:
        mock_api.return_value = fake_drug_1
        found_drug = find_or_fetch_drug('fake drug', connection)
        assert found_drug['drug_name'] == 'fake drug'

        mock_api.assert_called_once_with('fake drug')

    cursor.execute('DELETE FROM drugs WHERE drug_name = %s',
                   ('fake drug',))

    connection.commit()
    cursor.close()
    connection.close()

def test_drug_loaded_after_api_fetch():
    connection = connect_to_db()
    cursor = connection.cursor(row_factory=dict_row)

    with patch('pipeline.get_drug_data') as mock_api:
        with patch('pipeline.load_drug') as mock_load:
            mock_api.return_value = fake_drug_1

            drug = clean_drug_data(fake_drug_1)
            find_or_fetch_drug(drug['drug_name'], connection)

            mock_load.assert_called_once_with(drug, connection)

    connection.close()
    cursor.close()