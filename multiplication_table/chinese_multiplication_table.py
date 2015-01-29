# -*- coding: utf-8 -*-  
'''Nine-Nine Multiplication Table in Chineses'''

chineses_table = {'':'', 0:'零', 1:'一', 2:'二', 3:'三', 4:'四', 5:'五', 6:'六', 7:'七', 8:'八', 9:'九', 10:'十'}

def multiplication_table():
	for x in range(1, 10):
		for y in range(1, 10):
			result = x*y
			chinese_digit_in_tens = get_chinese_digit_in_tens(get_digit_in_tens(result))
			chinese_digit_in_ones = chineses_table.get(get_digit_in_ones(result))
			chineses_result = '%s%s' % (chinese_digit_in_tens,chinese_digit_in_ones)
			print('%s 乘以 %s 等於：%s' % (chineses_table.get(x), chineses_table.get(y), chineses_result))

def get_digit_in_tens(number):
	return number / 10

def get_chinese_digit_in_tens(number):
	if number is 0: return ''
	elif number is 1:
		return chineses_table.get(10)
	else:
		return '%s十' % chineses_table.get(number)

def get_digit_in_ones(number):
	digit = number % 10
	if digit is 0:
		return ''
	else:
		return digit

multiplication_table()
