#! /usr/bin/python
import os

var1 = "Hello"
var2 = "world"
var3 = 30
var4 = 50.0

total = var3 + var4
str_total = var1 + var2
str_total1 = var1 * var3
print total
print str_total
print str_total1
print var1 + " " + var2 + str(total)
if var3 ==  3:
	print  "Match with value"
elif var3 ==5:
	print "i got 5"
elif var3 > 10:
	print " i got more than 10"
else:
	print "mismatch !!!!"

print len(str_total)
name = raw_input("Whats your name?")
myCurrentWorkingDir = os.system("mkdir -p awadhesh")
if myCurrentWorkingDir != 0:
	print "unsuccessfull command"
else :
	print "command Successful!!!"
print "my Directory : " + str(myCurrentWorkingDir)

print "My name is " + name
if (name.upper() == "NARI"):
	print "name matched"
else :
	print "not matched"
