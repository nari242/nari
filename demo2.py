#! /usr/bin/python
import os
import sys

myInput = sys.argv
print myInput
myName = sys.argv[1]
print myName
index = 0
for localVar in myInput:
	print "Index " + str(index) + " : " + localVar
	if (localVar.lower() == "nari"):
		print "Finally got myyyy vaaaaaaaaaaaaarible " + " : " + str(index)
		exit()
	index = index + 1

num = int(sys.argv[4])
while num > 0 :
	print num
	num = num - 1		
