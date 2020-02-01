
# Import socket module
from socket import *
import sys # In order to terminate the program

serverName = 'localhost'



# Bind the socket to server address and server port
clientSocket = socket(AF_INET, SOCK_STREAM)
serverPort = int(input("Server Port : "))
serverName = input("server address : ")
clientSocket.connect((serverName, serverPort))
sentence = input(' Input lower case sentence: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)

print('From server: ', modifiedSentence.decode())
clientSocket.close()
