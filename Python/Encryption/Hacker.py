def readFromFile(filename):
	fileOpen = open(filename + ".txt", 'r')
	output = eval(fileOpen.read())
	return output

def decrypt(message, key):
	output = []
	for num in message:
		char = int(num)
		output.append(char / key)
	
	conv = ''.join(numbersToString(output))
	return conv

def numbersToString(message):
	return [chr(char) for char in message]

filename = raw_input("Filename: ")
content = readFromFile(filename)

#method one
print "*****************************"
print "Method 1 :"
space = min(content)
key = space/32
print "Key is : " + str(key)
print decrypt(content, key)
print "*****************************"

choice = raw_input("continue? (y/n) :")

if choice == 'y':
	#method 2
	print "XXXXXXXXXXXXXXXXXXXX"
	print "Look For 'a' "
	for alpha in content:
		key = alpha/97
		print "Key is : " + str(key)
		print decrypt(content, key)
		print "**********************"

choice = raw_input("continue? (y/n) :")

if choice == 'y':
	#method 2
	print "XXXXXXXXXXXXXXXXXXXX"
	print "Look For 's' "
	for alpha in content:
		key = alpha/115
		print "Key is : " + str(key)
		print decrypt(content, key)
		print "**********************"



