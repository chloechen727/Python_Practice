# -*- coding: utf-8 -*-
# Note: This executes slowly. Need to save time, using LIST on factorial(n).

import os, sys

FIVE_STEPS = 5
THREE_STEPS = 3
ONE_STEPS = 1

def total_combination(n):
	if(n==0):
		return 1
	else:
		total_combination_result = 0

		for element_z in range(0, n//FIVE_STEPS+1, +1):
			tmp_value_without_each_fixed_z = n - FIVE_STEPS*element_z

			for element_y in range(0, tmp_value_without_each_fixed_z//THREE_STEPS+1, +1):
				element_x = tmp_value_without_each_fixed_z - THREE_STEPS*element_y
				
				this_conmbination = combination(element_x, element_y, element_z)
				total_combination_result = total_combination_result + this_conmbination

		return total_combination_result


def combination(x, y, z):
	return (factorial(x+y+z)/(factorial(x)*factorial(y)*factorial(z)))

# TO-DO: use LIST
def factorial(number):
	total = 1
	for element in range(number, 1, -1):
		total = total * element
	return total

n = int(sys.argv[1])

print ('Total combination of ' + str(n) + ' stairs : ' + str(total_combination(n)))