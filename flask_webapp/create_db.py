import sqlite3

conn = sqlite3.connect('templogger.db')
print "Opened database successfully"

conn.execute('CREATE TABLE temperature (id INTEGER PRIMARY KEY AUTOINCREMENT , timestamp INTEGER, temp REAL)')
print "Table created successfully"
conn.close()