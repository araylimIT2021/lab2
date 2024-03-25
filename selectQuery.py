from random import randint
import mysql.connector
import time
def connect_to_db():
    return mysql.connector.connect(host="localhost", user="root", password="", database="lab2")
def totsl_number_of_entries(cursor):
    query = "SELECT COUNT(*) FROM table2"
    cursor.execute(query)
    total_number_of_entries = cursor.fetchone()
    return total_number_of_entries[0]


database = connect_to_db()
database.autocommit = False
myCursor = database.cursor()
time1 = time.time()
result = totsl_number_of_entries(myCursor)
time2 = time.time()
print("4a) The total number of entries in table2 is equal to ", result, "Time taken to execute query is: ", time2 - time1)
with open("output.txt", "w") as f:
    time3 = time.time()
    query = "SELECT * FROM table2"
    myCursor.execute(query)
    all_entries = myCursor.fetchall()
    for el in all_entries:
        f.write(str(el))
    time4 = time.time()
    f.write(str(f"4b) Getting all entries in the table. Time taken to execute query is: , {time4 - time3}"))
with open("output2.txt") as f:
    time5 = time.time()
    query = "SELECT * FROM table2 WHERE a1 LIKE '111%'"
    myCursor.execute(query)
    result = myCursor.fetchall()
    time6 = time.time()
    f.write(str(f"4c) Getting entries that matches specific entries in the table. {result} . Time taken to execute query is: , {time6 - time5}"))


database.disconnect()