from random import randint
import mysql.connector
import time
def commitAfterEachInsert(query, cursor):
    time1 = time.time()
    for i in range(0, 100000, 1):
        a1 = randint(0, 1000)
        a2 = randint(0, 1000)
        a3 = randint(0, 1000)
        a4 = randint(0, 1000)
        cursor.execute(query, (a1, a2, a3, a4))
        database.commit()
    time2 = time.time()
    total_time = time2 - time1
    print("Query time", total_time, "seconds ")

def commitAfterAllInsert(query, cursor):
    time1 = time.time()
    for i in range(0, 100000, 1):
        a1 = randint(0, 1000)
        a2 = randint(0, 1000)
        a3 = randint(0, 1000)
        a4 = randint(0, 1000)
        cursor.execute(query, (a1, a2, a3, a4))
    database.commit()
    time2 = time.time()
    total_time = time2 - time1
    print("Query time", total_time, "seconds ")

def commitAfterNthInsert(query, cursor, nthValue):
    time1 = time.time()
    for i in range(0, 100000, 1):
        a1 = randint(0, 1000)
        a2 = randint(0, 1000)
        a3 = randint(0, 1000)
        a4 = randint(0, 1000)
        cursor.execute(query, (a1, a2, a3, a4))
        if (i+1) % nthValue == 0:
            database.commit()
    time2 = time.time()
    total_time = time2 - time1
    print("Query time", total_time, "seconds ")

# connection to the database
database = mysql.connector.connect(host="localhost", user="root", password="", database="lab2")
database.autocommit = False
cursor = database.cursor()

# insert type query
query = "INSERT INTO table2 (a1, a2, a3, a4) VALUES (%s, %s, %s, %s)"

#commitAfterEachInsert(query, cursor) # Query time 231.1017336845398 seconds
#commitAfterAllInsert(query, cursor) # Query time 11.142678260803223 seconds
#commitAfterNthInsert(query, cursor, 100) # Query time 27.0556857585907 seconds

#3rd task
#for each function in 2nd step perform a connection error test.
#Estimate how many data was initially in db - done
# Then start random data insertion
# turn off or disconnect from the database management system.
# evaluate how many records have been inserted into the database final count of data in db
def countOfExistingRecords(cursor):
    cursor.execute("SELECT COUNT(*) FROM table2")
    result = cursor.fetchone()
    return result[0]

countOfExistingRecords(cursor)

