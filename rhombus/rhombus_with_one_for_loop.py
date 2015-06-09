# -*- coding: utf-8 -*-  
# call it : python rhombus.py {number}

import os, sys

def print_rhombus(number):
	if ((((number-3)%2)==0) and (number>=3)):
		middle = number/2
		space = middle
		for i in range(number):
			# print upon triangle
			if i<=middle:
				print (' '*space+'*'*(1+i*2))
				if space>=1: space=space-1
			# print inverted tiangle
			else:
				space=space+1
				print (' '*space+'*'*(number-space*2))
	else:
		print 'Sorry, it can not form a rhombus.'

n = int(sys.argv[1])
print_rhombus(n)
