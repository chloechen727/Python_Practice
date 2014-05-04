# -*- coding: utf-8 -*-
# Target: Get the sum of multiplication of string value and their order.
# Run command as: python get_the_sum_of_multiplication_of_string_value_and_their_order.py sample1.dat

import sys
import string

def read_input_file_and_get_the_sorted_string(sample_data):
	f = open(sample_data, 'r')
	string_input = f.read()
	f.close()
	list_input = sorted([x.strip('"') for x in string_input.split(',')])
	print 'The sorted input: ' , list_input
	return list_input

def get_dict_A_to_Z():
	list_A_to_Z = ' '.join(string.ascii_uppercase).split()
	list_1_to_26 = [x+1 for x in range(26)]
	dict_A_to_Z = dict(zip(list_A_to_Z, list_1_to_26))
	return dict_A_to_Z

def get_the_sum_of_multiplication_of_string_value_and_their_order(list_input, dict_A_to_Z):
	output_sum = 0
	
	for i in range(len(list_input)):
		list_string = []
		[list_string.append(dict_A_to_Z.get(chart)) for chart in list_input[i]]
		string_value = reduce(lambda x,y:x+y, list_string) * (i+1)
		list_input[i] = string_value
	print 'The input list value: ', list_input

	output_sum = reduce(lambda x,y:x+y, list_input)
	return output_sum

if __name__ == '__main__':
	sample_data = sys.argv[1]
	list_input = read_input_file_and_get_the_sorted_string(sample_data)
	dict_A_to_Z = get_dict_A_to_Z()
	result = get_the_sum_of_multiplication_of_string_value_and_their_order(list_input, dict_A_to_Z)
	print 'The result: ', result