import psycopg2
from psycopg2 import sql

# Параметры подключения к базе данных PostgreSQL
db_params = {
    'dbname': 'postgres',
    'user': 'admin',
    'password': 'admin',
    'host': '',
    'port': ''
}

def create_database():
    conn = psycopg2.connect(**db_params)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute('CREATE DATABASE request_db')
    cursor.close()
    conn.close()

def create_table():
    db_params['dbname'] = 'request_db'
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id SERIAL PRIMARY KEY,
            request_number INTEGER
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

def add_request(request_number):
    db_params['dbname'] = 'request_db'
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO requests (request_number) VALUES (%s)', (request_number,))
    conn.commit()
    cursor.close()
    conn.close()

# Создаем базу данных и таблицу
create_database()
create_table()

# Добавляем запись с номером запроса 1
add_request(1)
print("Запись добавлена: номер запроса 1")