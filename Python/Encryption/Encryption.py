#takes message and returns a list of ASCII numbers
def stringToNumbers(message):
	return [ord(char) for char in message]

def numbersToString(message):
	return [chr(char) for char in message]


import random 
randNum = int(random.random()*1000000000000)

def encrypt(message, key):
	output = []
	conv = stringToNumbers(message)

	for char in conv:
		num = int(char)
		output.append(num * key)

	return output

def decrypt(message, key):
	output = []
	for num in message:
		char = int(num)
		output.append(char / key)
	
	conv = ''.join(numbersToString(output))
	return conv


def writeToFile(content, filename, key):
	msgFile = open( filename+'.txt', 'w')
	keyFile = open(filename+"-key.txt", 'w')

	line = msgFile.write(str(content))
	line2 = keyFile.write(str(key))

def readFromFile(filename):
	fileOpen = open(filename + ".txt", 'r')
	output = eval(fileOpen.read())
	return output

def lookForKey(filename):
	fileOpen = open(filename + "-key.txt", 'r')
	output = eval(fileOpen.read())
	return output

def runProgram():
	repeat = 'y'
	while repeat == 'y':
		print "Hi! What would you like to do?"
		print "1. Encrypt message"
		print "2. Decrypt message"
		choice = raw_input("Choice: ")
		if choice == "2":
			print 'Decryption Time!'
			filename = raw_input("Filename: ")
			encMsg = readFromFile(filename) 
			key = int(lookForKey(filename))
			decMsg = decrypt(encMsg, key)
			print decMsg
		if choice == '1':

			print "Encryption Time!"

			filename = raw_input("Filename: ")
			message = raw_input("Message: ")
			key = randNum
			encMsg = encrypt(message, key)
			writeToFile(encMsg, filename, key)
		repeat = raw_input("Would you like to repeat? (y/n): ")
	print "Goodbye!"



runProgram()














