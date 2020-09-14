#!/bin/python3

import subprocess

y = int(input("de cite ori sa se execute comanda "))

x = 1

while x <= y:
	x += 1
	subprocess.run(["python3", "impulse.py", "--target", "37367284201", "--method", "SMS"] )
	print(x)
