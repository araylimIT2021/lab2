from random import randint
import mysql.connector
import time
def connect_to_db():
    return mysql.connector.connect(host="localhost", user="root", password="", database="lab2")
def insert_random_data(cursor):
    query = "INSERT INTO table2 (a1, a2, a3, a4) VALUES (%s, %s, %s, %s)"
    for i in range(0, 100000, 1):
        a1 = randint(0, 1000)
        a2 = randint(0, 1000)
        a3 = randint(0, 1000)
        a4 = randint(0, 1000)
        cursor.execute(query, (a1, a2, a3, a4))
        database.commit()
        #if i == 5000:
        #    database.close()
        #    print("Simulated connection error after 5000 inserts")
def count_of_existing_records(cursor):
    cursor.execute("SELECT COUNT(*) FROM table2")
    result = cursor.fetchone()
    return result[0]
# connection to the database

try:
    database = connect_to_db()
    database.autocommit = False
    myCursor = database.cursor()
    existing_records = count_of_existing_records(myCursor)
    print("Existing records in the table before insertion: ", existing_records)
    insert_random_data(myCursor)
except mysql.connector.Error as err:
    print("Error", err)
    database = connect_to_db()
    cursor = database.cursor()
    new_records = count_of_existing_records(cursor) - existing_records
    print("Count of newly inserted records to db: ", new_records)
except KeyboardInterrupt as err:
    print("Error, reconnecting to db", err)
    database = connect_to_db()
    cursor = database.cursor()
    new_records = count_of_existing_records(cursor) - existing_records
    print("Count of newly inserted records to db: ", new_records)
finally:
    if 'database' in locals():
        database.close()