import os
import mysql.connector
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Connect to the database
def get_db_connection():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        autocommit=True
    )
    return connection


# Execute a query that returns data
def db_query(sql, params=None):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, params)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


# Insert into the database
def db_insert(sql, params=None):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(sql, params)
    last_row_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return last_row_id


# Delete from the database
def db_delete(sql, params=None):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(sql, params)
    cursor.close()
    connection.close()


# Update the database
def db_update(sql, params=None):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(sql, params)
    cursor.close()
    connection.close()
