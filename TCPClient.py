
# Import socket module
from socket import *
import sys # In order to terminate the program

print("server_start")

def post(board_width,board_height):

    good_input = 0

    #validate note
    while good_input == 0:

        #ask user for note
        print("\n--Enter note to be posted ex - 'POST 2 3 10 20 white Meeting next Wednesday from 2 to 3--\n")
        note = input("Enter Note : ")
        correct_input = note.split(" ")

        #this is to make sure the note itself is within the board defined
        width = int(correct_input[1]) + int(correct_input[3])
        height = int(correct_input[2]) + int(correct_input[4])

        check_input = correct_input[0] == "POST" and width <= int(board_width) and height <= int(board_height)

        if(check_input):
            good_input = 1
            return note


def pin(coords,noteList):
    

# Bind the socket to server address and server port
clientSocket = socket(AF_INET, SOCK_STREAM)

#ask user for port and name
serverPort = int(input("Server Port : "))
serverName = input("server address : ")

#connect to socket and send server info
clientSocket.connect((serverName, serverPort))
formattedMessage = clientSocket.recv(1024)

#grabs info needed to to client functions
print('From server: ', formattedMessage.decode())
formattedMessage = formattedMessage.decode().split(" ")

#get values of board
board_width = formattedMessage[1]
board_height = formattedMessage[2]

#shows all options client can choose
print("\n-----------------OPTIONS-------------\n")
print("1. POST\n")
print("2. GET\n")
print("3. PIN/UNPIN\n")
print("4. CLEAR\n")
print("5. DISCONNECT\n")
print("\n---USE NUMBERS TO PICK OPTION---\n")

good_input = 0

#validate an actual option is chosen
while good_input == 0:

    option = int(input("Enter Option (1-5) : "))

    if(option == 1 or option == 2 or option == 3 or option == 4 or option == 5):
        good_input = 1

#check which options and respond accordingly
if option == 1:
    note = post(board_width,board_height)
    message = "1 " + note
    #send message with note and option dictated
    clientSocket.send(message.encode())

elif option == 5:
    
    message = "5 "
    #send message with option
    clientSocket.send(message.encode())
    clientSocket.close()

