from graphics import*
from time import*
from random import*

#1)
def remove_punct(the_line):
	new_line = the_line.lower()
	punctuation = ",.\"?!':;"
	for symbol in punctuation:
		new_line= new_line.replace(symbol,"")
	return new_line

def process_line(the_line):
	no_punct = remove_punct(the_line)
	word_list = no_punct.split()
	return word_list

def process_file(filename):
	the_file = open(filename,"r")
	set=[]
	for line in the_file:
		answer = process_line(line)
		set.append(answer)
	return(set)

def yellow_func(file):
	a=process_file(file)	
	for x in a:
		if "yellow" in x:
			print("Found Yellow")

yellow_func("testfile7.txt")

#2)
def general_process_file(filename, word):
	a=process_file(filename)
	n=0	
	for x in a:
		y=len(a)
		if word in x:
			print(filename)
			print(word)
			print("yes")
		else:
			n=n+1
			if n==y:
				print(filename)
				print(word)
				print("no")

general_process_file("testfile7.txt", "yellow")

general_process_file("testfile7.txt", "apple")

#3)

import os

#I'm going to create a function called general_process2 that stops finding the word after having found it a single time. 

def general_process_file2(filename, word):
	a=process_file(filename)
	n=0
	r=0	
	for x in a:
		y=len(a)
		if word in x and r==0:
			print(filename)
			print(word)
			print("yes")
			r=1
		else:
			n=n+1
			if n==y:
				print(filename)
				print(word)
				print("no")

filenames= os.listdir("William")

for name in filenames:
	general_process_file2("William/"+name, "ophelia")

#4)

def general_process_file3(filename, word):
	a=process_file(filename)
	n=0
	s=[]	
	for x in a:
		y=len(a)
		if word in x:
			s.append(word)
		else:
			n=n+1
			if n==y:
				print(filename)
				print(word)
				print("0 times")
	l=len(s)
	if n!=y:
		print(filename)
		print(word)
		print("showed up this many times:")
		print(l)

general_process_file3( "testfile7.txt", "sugar")

#5)
	
for name in filenames:
	general_process_file3("William/"+name, "death")


input("press a key to continue")
