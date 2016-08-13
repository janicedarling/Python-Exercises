def urlify(s):
	chars = list(s)
	index = -1
	for x in chars:
	    index = index + 1
	    if x == ' ':
	        chars[index] = '%'
	        chars.insert((index + 1), '2')
	        chars.insert((index + 2), '0')
	return ''.join(chars)

'''
def urlify(s):
	newString = s.replace(' ', "%20")
	return newString
'''

print(urlify("My dog"))

		
