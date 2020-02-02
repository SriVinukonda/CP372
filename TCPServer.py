# Import socket module
from socket import *
import sys # In order to terminate the program

#intialize note_list
note_list = []
colors = []

class note():
	message = ""
	coords = []
	dimensions = []
	color = []

def createNote(messageIn,coordsIn,dimensionsIn, colorIn):
	stickyNote = note()
	stickyNote.message = messageIn
	stickyNote.coords = coordsIn
	stickyNote.dimensions = dimensionsIn
	stickyNote.color = colorIn

	return stickyNote

def post(message):

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

def get_pins(message):

	message = message.split(" ")
	print(message)
	message_value = ""
	coordinates = []
	color = ""

	i = 0

	#go through message and grab important details
	while i < len(message):
		
		if len(message[i]) >= 6 and message[i][:6] == "color=":
			color = message[i][6:]

		elif len(message[i]) >= 9 and message[i][:9] == "contains=":
			coordinates = [int(message[i+1]),int(message[i+2])]

		elif len(message[i]) >= 10 and message[i][:10] == "refersTo":
			message_value = message[i][10:]

		i+=1


	#check what is filled and find coordinating notes
	if(message_value != "" and coordinates != [] and color != ""):

		for i in note_list:
			if(color == i.color and message_value in i.message and coordinates == i.coords):
				print(i.message)

	elif(message_value != "" and coordinates != []):

		for i in note_list:
			if(message_value in i.message and coordinates == i.coords):
				print(i.message)

	
	elif(message_value != "" and color != ""):

		for i in note_list:
			if(color == i.color and message_value in i.message):
				print(i.message)

	
	elif(coordinates != [] and color != ""):

		for i in note_list:
			if(color == i.color and coordinates == i.coords):
				print(i.message)

	elif(coordinates != []):

		for i in note_list:
			if(coordinates == i.coords):
				print(i.message)

	elif(color != ""):

		for i in note_list:
			if(color == i.color):
				print(i.message)

	elif(message_value != ""):

		for i in note_list:
			if(message_value in i.message):
				print(i.message)

	

	


				




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

# Listen to at most 1 connection at a time
serverSocket.listen(1)

print ('The server is ready to receive')

# Server should be up and running and listening to the incoming connections

#while server is on keep intaking client sockets
while True:

	print('The server is ready to receive')

	# Set up a new connection from the client
	connectionSocket, addr = serverSocket.accept()

	#convert list to string to send info to client
	formatted_message = ' '.join(str(e) for e in sys.argv[1:])

	#send in info client needs - size of board,color etc
	connectionSocket.send(formatted_message.encode())

	try:
		message = connectionSocket.recv(1024).decode()
		option = int(message[0])
		print(message)
	
		#if option was 2 then get close , 3 note
		if(option == 2):
			#closing all connections
			connectionSocket.close()

		if(option == 3):
			message = ' '.join(message.split(" ")[2:])
			post(message)

		elif(option == 4):
			get_pins(message[1:])

		
		
	except:
		print("1")

		


serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data
