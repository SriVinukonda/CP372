# Import socket module
from socket import *
import sys # In order to terminate the program


class note():
	message = ""
	coords = []
	dimensions = []
	color = ""
	pinned = 0
	pins = []

def createNote(messageIn,coordsIn,dimensionsIn, colorIn):
	stickyNote = note()
	stickyNote.message = messageIn
	stickyNote.coords = coordsIn
	stickyNote.dimensions = dimensionsIn
	stickyNote.color = colorIn

	return stickyNote

def post(message,note_list):

	message = message.split(" ")
	color = []

	#use note message to dictate all values
	coords = [int(message[0]),int(message[1])]
	dimensions = [int(message[2]),int(message[3])]
	
	#check for values of colors are in what is allowed - rest are apart of message
	index = 4

	colorISALLOWED = 0
	
	while colorISALLOWED == 0:

		if message[index] in colors:
			color.append(message[index])
			index+=1
		
		else:

			colorISALLOWED = 1

	#rest is part of message
	message = ' '.join(message[index:])

	#create note
	stickyNote = createNote(message,coords,dimensions,color)

	#append note
	note_list.append(stickyNote)

def get(message, noteList, pinList):
	print(message)
	returnList = []
	splitString = message.split(" ")

	if(len(splitString) == 7):
		print("INSIDE get FIRST IF")
		i = 0
		j = 0

		color = splitString[2].split("=")
		for i in range(len(noteList)):	
			print("INSIDE GET FIRST FOR STATEMENT")
			print("{0:} == {1:}".format(noteList[i].color[0], color[1]))
			if(noteList[i].color[0] == color[1]):
				
				currentCoords = noteList[i].coords
				for j in range(len(currentCoords)):
					print("INSIDE GET SECOND FOR STATEMENT")
					if(int(currentCoords[j]) == int(splitString[4])):
						if(int(currentCoords[j][1]) == int(splitString[5])):
							returnList.append(noteList[i])
	
		i = 0
		rmv = 1
		for i in range(len(returnList)):
			for word in returnList.message:
				if(word == splitString[6].split("=")[1]):
					rmv = 0
					break
			if (rmv == 1):
				returnList.pop(i)
	elif(len(splitString) == 5):
		if(splitString[2].split("=")[0] == "color"):
			i = 0
			for i in range(noteList):
				currColor = splitString[2]
				if(noteList[0].color == currColor.split("=")[2]):
					returnList.append(noteList)
			
			for j in range(len(returnList)):
				if(int(currentCoords[j][0]) == int(splitString[4])):
					if(int(currentCoords[j][1]) == int(splitString[5])):
						returnList.append(noteList[i])
	
				
	elif(len(splitString) == 4):
		i = 0
		for i in range(len(noteList)):
			currColor = splitString[2]
			if(noteList[0].color == currColor.split("=")[2]):
				returnList.append(noteList)
		
		i = 0
		rmv = 1
		for i in range(len(returnList)):
			for word in returnList.message:
				if(word == splitString[3].split("=")[1]):
					rmv = 0
					break
			if (rmv == 1):
				returnList.pop(i)
	
	l = 0
	print("END OF GET INSIDE SERVER")
	# for l in range(len(returnList)):
	# 	print("INSIDE OF FOR LOOP AT THE END OF GET")
	# 	print(returnList[l])

def clear(noteList):

	i = None
	for i in noteList:
		if(i.pinned == 0):
			noteList.remove(i)




def pin(coords,noteList,pinList):
	i = 0
	# print("Inside pin in server",coords[0],coords[1])
	j = 0
	input = 1
	while (j < len(pinList)):
		if(int(pinList[j][0]) == int(coords[0]) and int(pinList[j][1]) == int(coords[1])):
			input = 0
			print("That pin already exists")
			break
		j += 1
	if (input == 1):
		print("INSIDE PIN INSIDE INPUT == 1")
		pinList.append(coords)
			

	while (i < len(noteList) and input == 1):
		if(int(noteList[i].coords[0]) <= int(coords[0]) and int(coords[0]) <= int(noteList[i].coords[0])+int(noteList[i].dimensions[0])):
			if(int(noteList[i].coords[1]) <= int(coords[1]) and int(coords[1]) <= int(noteList[i].coords[1])+int(noteList[i].dimensions[1])):
				print("Inside the if statement(s)")
				noteList[i].pinned = 1
				noteList[i].pins.append(coords)
				print("Note at {:} has been pinned.".format(noteList[i].coords),coords)
		i += 1

def unPin(coords,noteList,pinList):
	i = 0
	while(i < len(noteList)):
		if(len(noteList[i].pins) > 1):
			j = 0
			while (j < len(noteList[i].pins)):
				temp = noteList[i].pins[j]
				if(temp[0] == coords[0] and temp[1] == coords[1]):
					rmv = noteList[i].pins.pop(j)
					pinList.remove(rmv)
					noteList[i].pinned = 0
					print("Note at {:} has been unpinned".format(noteList[i].coords),coords)
				j+=1

		else:
			if(len(noteList[i].pins) == 1):
				temp = noteList[i].pins[0]
				if(temp[0] == coords[0] and temp[1] == coords[1]):
					rmv = noteList[i].pins.pop(0)
					pinList.remove(rmv)
					noteList[i].pinned = 0
					print("Note at {:} has been unpinned".format(noteList[i].coords),coords)

		i+=1


#intialize note_list
note_list = []
pin_list = []
colors = []


# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
server_start = " "

#used to get all info from command line - board size , color  etc
if(len(sys.argv) > 4):
	serverPort = int(sys.argv[1])
	board_width = int(sys.argv[2])
	board_height = int(sys.argv[3])
	colors = sys.argv[4:]

	server_start = sys.argv[1] + " "		
else:
	print("not enough info provided or incorrect format")
	exit(0)

#server socket initialization
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the socket to server address and server port
serverSocket.bind(("", serverPort))

# Listen to at most many connection at a time
serverSocket.listen()

print ('The server is ready to receive')

# Set up a new connection from the client
connectionSocket, addr = serverSocket.accept()

print('The server is ready to receive inside while')

#convert list to string to send info to client
formatted_message = ' '.join(str(e) for e in sys.argv[1:])


print("formatted_message",formatted_message)
#send in info client needs - size of board,color etc
connectionSocket.send(formatted_message.encode())

# Server should be up and running and listening to the incoming connections

#while server is on keep intaking client sockets
while True:

	try:
		message = connectionSocket.recv(1024).decode()
		print("Message received: ",message.split(" ")[0])
		option = int(message.split(" ")[0])
	
		print("INSIDE OPTIONS\n")
		#if option was 2 then get close , 3 note
		if(option == 2):
			#closing all connections
			print("disconnect -- need")
			connectionSocket.close()
			break
		elif(option == 3):
			print()
			message = ' '.join(message.split(" ")[2:])
			print(message)
			post(message, note_list)

		elif(option == 4):
			

			get(message,note_list,pin_list)
		elif(option == 5):
			# print("INSIDE OPTION 5\n")
			
			decodedMessage= message.split(" ")
			print("Message inside server in option 5",decodedMessage[1:])
			pin(decodedMessage[1:],note_list,pin_list)
		elif(option == 6):
			# print("INSIDE OPTION 6\n")
			decodedMessage= message.split(" ")
			print("Message inside server in option 6",decodedMessage[1:])
			unPin(decodedMessage[1:],note_list,pin_list)
		elif(option == 7):
			clear()
    		
		
		
	except error as e:
		print(e.strerror)
		print("Error")

		


serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data
