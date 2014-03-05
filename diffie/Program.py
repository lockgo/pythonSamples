#import urllib

def diffie(a, p, g, b):
	Alice = (g**a) % p 
	Bob = (g**b) % p
	s = (Bob**a) % p
	t = (Alice**b) % p
	print "Alice is %d!\n" 	%Alice
	#print "g to the a is %d\n"  %testout
	print "and Bob is %d\n"	%Bob
	print "and s is %d\n"  	%s
	print "and t is %d"	%t

inputing = raw_input("please input a\n")
a = int(inputing)
inputing = raw_input("please input p\n")
p = int(inputing)
inputing = raw_input("please input g\n")
g = int(inputing)
inputing = raw_input("please input b\n")
b = int(inputing)
diffie(a, p, g, b);

inputing = raw_input("please input b\n")
itsover = int(inputing)

