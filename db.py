import psycopg
from psycopg.types.json import Jsonb
from psycopg.rows import dict_row

def connect_to_db():
    connection = psycopg.connect(
        dbname='drug_information',
        user='alexiskim',
        host='localhost',
        port='5432'
    )

    return connection

def load_drug(drug, connection):

    with connection.transaction():
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO drugs (' \
            '"drug_name", ' \
            '"generic_name",' \
            '"manufacturer",' \
            '"purpose",' \
            '"warnings",' \
            '"dosage_and_administration",' \
            '"active_ingredient") ' \
            'VALUES(%s, %s, %s, %s, %s, %s, %s)', 
            (drug['drug_name'],
            drug['generic_name'],
            drug['manufacturer'],
            Jsonb(drug['purpose']),
            Jsonb(drug['warnings']),
            Jsonb(drug['dosage_and_administration']),
            Jsonb(drug['active_ingredient']))

        )
    

def get_drug(drug_name, connection):
    cursor = connection.cursor(row_factory = dict_row)

    cursor.execute(
        'SELECT * FROM drugs WHERE drug_name = %s',
        (drug_name,)
    )

    obtained = cursor.fetchone()
    cursor.close()

    return obtained