# -*- coding: utf-8 -*-  
# Note: only support combination(1000), or need to setrecursionlimit(n)

import os, sys

waling_stairs_dict = {'0':1, '1':1, '2':1, '3':2, '4':3}

def combination(n):
	if(str(n) in waling_stairs_dict):
		return waling_stairs_dict[str(n)]
	else:
		result = combination(n-1) + combination(n-3) + combination(n-5)
		waling_stairs_dict[str(n)] = result
		return result

n = int(sys.argv[1])

print ('Total combination of ' + str(n) + ' stairs : ' + str(combination(n)))