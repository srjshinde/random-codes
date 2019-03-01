import sqlite3

conn = sqlite3.connect('database.db')
print "Opened database successfully";

conn.execute('CREATE TABLE data (id INTEGER PRIMARY KEY AUTOINCREMENT, temperature REAL, humidity REAL)')
print "Table created successfully";
conn.close()