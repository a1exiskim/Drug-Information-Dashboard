import psycopg
from psycopg.types.json import Jsonb

def connect_to_db():
    connection = psycopg.connect(
        dbname='drug_information',
        user='alexiskim',
        host='localhost',
        port='5432'
    )

    return connection

def load_drug(drug, connection):
    cursor = connection.cursor()

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

    connection.commit()
    cursor.close()
