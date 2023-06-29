#  Write a program to check if two strings are a rotation of each other?

def checkString(s1, s2, indexFound, Size):
	for i in range(Size):
		if(s1[i] != s2[(indexFound + i) % Size]):
			return False

	return True
s1 = "abcd"
s2 = "cdab"

if(len(s1) != len(s2)):
	print("s2 is not a rotation on s1")

else:

	indexes = [] 
	Size = len(s1)
	firstChar = s1[0]
	for i in range(Size):
		if(s2[i] == firstChar):
			indexes.append(i)

	isRotation = False
	for idx in indexes:

		isRotation = checkString(s1, s2, idx, Size)

		if(isRotation):
			break

	if(isRotation):
		print("Strings are rotations of each other")
	else:
		print("Strings are not rotations of each other")


