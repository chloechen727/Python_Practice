# -*- coding: utf-8 -*-
# Target: Exame if the tag is normal or not.
# Run command as: python exame_tags.py "<a><a></a><a></a></a>" or python exame_tags.py "<a"

import sys
def isTagsNormal(element):
	caculate = 0
	while (len(element) != 0):
		if (element.startswith('<a>')):
			caculate += 1
			element = element[3:]
		elif (element.startswith('</a>')):
			caculate -= 1
			element = element[4:]
		# If there's any abnormal tag, return false.
		else:
			return False
		# If the end tag appears before the head tag, return false.
		if (caculate < 0):
			return False

	# If head tags number isn't equal to end tags, return false.
	if (caculate > 0):
		return False
	elif (caculate == 0):
		return True

if __name__ == '__main__':
	sample_data = sys.argv[1]
	result = isTagsNormal(sample_data)
	print 'The result: ', result