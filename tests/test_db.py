from db import connect_to_db, load_drug
from db import get_drug
from transform import clean_drug_data
from tests.test_transform import fake_drug_1
from psycopg.rows import dict_row


def test_loading_drug():
    connection = connect_to_db()
    cursor = connection.cursor(row_factory = dict_row)

    cleaned_drug = clean_drug_data(fake_drug_1)

    load_drug(cleaned_drug, connection)

    cursor.execute('DELETE FROM drugs WHERE drug_name = %s',
                   ('fake drug',))
    connection.commit()
    cursor.close()
    connection.close()


def test_get_drug():
    connection = connect_to_db()
    cursor = connection.cursor(row_factory = dict_row)

    clean_drug = clean_drug_data(fake_drug_1)

    load_drug(clean_drug, connection)

    fake_drug_row = get_drug('fake drug', connection)
    assert fake_drug_row['drug_name'] == 'fake drug'
    assert fake_drug_row['warnings'] == ['fake warning']

    cursor.execute('DELETE FROM drugs WHERE drug_name = %s', 
                   ('fake drug',))

    connection.commit()
    cursor.close()
    connection.close()


def test_get_drug_not_found():
    connection = connect_to_db()
    cursor = connection.cursor(row_factory = dict_row)

    empty_drug_row = get_drug('ur mom', connection)
    assert empty_drug_row is None

    cursor.execute('DELETE FROM drugs WHERE drug_name = %s', 
                   ('fake drug',))

    connection.commit()
    cursor.close()
    connection.close()
