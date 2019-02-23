import sqlite3 as sql
import random
import time

while True:
    try:

        with sql.connect("templogger.db") as connection:
            cursor = connection.cursor()

            cursor.execute("INSERT INTO temperature ( timestamp, temp)VALUES( ?, ?)", (time.time(), random.randint(0, 55)))

            connection.commit()
            msg = "Record successfully added"
            time.sleep(4)
    except:

        connection.rollback()
        msg = "error in insert operation"

    finally:

        connection.close()