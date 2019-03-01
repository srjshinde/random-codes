from flask import Flask
from flask import request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/postjson', methods = ['POST'])
def postJsonHandler():

    if request.is_json:
        content = request.get_json(force=False)
        print (content)

        try:
            temp=content["temperature"]
            humi=content["humidity"]

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO data (temperature, humidity)VALUES(?, ?)",(temp, humi) )
                con.commit()
                return "Record successfully added"
        except:
            con.rollback()
            return "error in insert operation"

    else:
        return "could not valid JSON data. check header or data"


app.run(host="0.0.0.0", port= 5000,debug="on")