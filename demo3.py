#! /usr/bin/python
import sys
def myLengthPrint(localVarib):
	print localVarib
	print len(localVarib)

print len(sys.argv)

myValue = 10
Devops = "dev"
myList = ["Awadhesh","Nari",Devops,myValue]
#                0       1    2     3
myLengthPrint(myList)
print myList[1]
myList[1] = 'Narendra'
#print "my List : " + str(len(myList))
print "my List : " + str(myList)
for myLocal in myList:
	print myLocal

myTupple = ("Awadhesh","Nari",Devops,myValue)
print "my Tupple : " + str(myTupple)
#myTupple[1] = 'Narendra'
print myTupple
myLengthPrint(myTupple)

mydict = {}
mydict = {12: "Awadhesh", 23 : "Nari",24 : 'Devops'}
print mydict
print mydict[23]
mydict[23] = "Narendra"
print mydict
myLengthPrint(mydict)


myFileHandle = open('test.txt','r')
print "myFile content : ", myFileHandle.read()
#myFileHandle.write('Narendra\n')
myFileHandle.close()

