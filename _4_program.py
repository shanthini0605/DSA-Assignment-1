# Write a program to print the first non-repeated character from a string


def FirstNonRepeat(s):

	for i in s:

		if (s.find(i, (s.find(i)+1))) == -1:

			print("First non-repeating character is", i)

			break

	return

s = 'Data Structure and Algorithm'
FirstNonRepeat(s)
