
# Import socket module
from socket import *
import sys # In order to terminate the program

print("server_start")


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
clientSocket.close()

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


def post():

    print