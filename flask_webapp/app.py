from flask import Flask, render_template, request
import sqlite3 as sql
import threading
import random

update_interval=4

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome To Temperature Logging API"


@app.route('/get_temp')
def new_student():
    return "ghe temp..."


@app.route('/list')
def list_out():
    con = sql.connect("templogger.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from temperature")

    rows = cur.fetchall()
    return render_template("list.html", rows=rows)

def print_count():
    for i in range(0,10):
        print i
        time.sleep(0.5)


def update_db():
    while True:
        print "aat aloy.."
        try:
            with sql.connect("templogger.db") as connection:
                cursor = connection.cursor()

                cursor.execute("INSERT INTO temperature ( timestamp, temp)VALUES( ?, ?)", (time.time(), random.randint(0, 55)))

                connection.commit()
                print "Record successfully added"
                time.sleep(update_interval)

        except:
            print "nahi hot ae..."
            connection.rollback()

def print_count():
    for i in range(0,10):
        print i
        time.sleep(0.5)

def run_app():
    app.run(debug=True)


app_thread=threading.Thread(target=run_app())
db_thread=threading.Thread(target=print_count())
try:
    db_thread.start()
    app_thread.start()

except:
    print "locha ahe..."
finally:
    con.close()
    print "end"