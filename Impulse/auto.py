#!/bin/python3

import subprocess
import sqlite3



#Create data base
conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS victime(
		nume text,
		numar integer
		)
	""")
#introduce in data base
def data_input():
	numele = str(input("introduceti numele "))
	numar = int(input("introduceti numarul "))
	victime = [(numele, numar)]
	c.executemany("INSERT INTO victime VALUES (?,?)", victime)
	conn.commit()

#arata data base
def data_show():
	c.execute("SELECT rowid, * FROM victime")
	vic = c.fetchall()
	print("\nBaza de date\n")
	for item in vic:
		print(item)

#executa
def smsex(numar):
	x = 1
	y = int(input("de cite ori sa se execute comanda "))
	while x <= y:
		print(x)
		x += 1
		#subprocess.run(["python3", "impulse.py", "--target", "37367188891", "--method", "SMS"] )
		subprocess.run('python3 impulse.py --target %s --method SMS' %(numar), shell=True)

#executa din data base
def smsex_data():
	data_show()
	select = int(input("\nselectati id victimei\n"))

	c.execute("SELECT * FROM victime WHERE rowid = %s"%(select))
	vic = c.fetchall()
	for item in vic:
		numar = item[1]
	print("\n",numar)
	
	smsex(numar)

#executa o singura data
def smsex_one():
	numar = int(input("introduceti numarul"))
	smsex(numar)


def run():	
	option = int(input("\nOptiuni\n\n1. Introduceti in baza de date\n2. Arata baza de date\n3. Executati din baza de date\n4. Executati o singura data\n5. Restul\n\n"))
	if option == 1:
		data_input()
	elif option == 2:
		data_show()
	elif option == 3:
		smsex_data()
	elif option == 4:
		smsex_one()



#main

o=1

while o == 1:
	run()
	o = int(input("\nDoriti sa executati in continuare\n\n1. Da\n2. Nu\n\n"))








#c.execute("SELECT rowid, * FROM victime")

#print(c.fetchone()[1])
#print(c.fetchmany(3))
#print(c.fetchall())


#vic = c.fetchall()

#for row in vic:
#	print(vic)



conn.close()






