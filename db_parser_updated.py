#!/usr/bin/python

#use requirements.txt to install these dependancies
#Environment details are mentioned in file, environment.md

#SQLite version 0.0.1
import sqlite3

#msgpack version 1.0.0
import msgpack

#Functions to display or suppress debug messages
VERBOSE=False
def dprint(debugMsg):
	if VERBOSE:
		print(debugMsg)


#add DB filename in the bracket. Assumes the file to be present in the working directory
conn = sqlite3.connect('/var/data/events.db')
dprint("Opened database successfully\n")

#[WIP remove unecessary columns for the sake of execution speed]
cursor = conn.execute("SELECT boot_seq, event_id, event_type, uptime_sec, uptime_nsec, body FROM events where event_id > 59565 limit 10 ")

for row in cursor:
	print("ID = ", row[1])
	print("Type = ", row[2])

	#writes data to file, this is later read by the Unpacker 
	#To-DO: inefficient method, change it. Currently implemented because the Unpacker needs
	#object with read() method support.
	with open("data.msgpack", "wb") as dataFile:
		dataFile.write(row[5])

        #unpacks the multiple msgpack objects and returns a list of them
	with open("data.msgpack", "rb") as file:
		unp = msgpack.Unpacker(file)

		for data in unp:
			print(data)
			print("#########################################################################")

dprint("\n\nOperation done successfully")

#Do not forget this!
conn.close()
