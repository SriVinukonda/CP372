
# Import socket module
from socket import * 
import sys # In order to terminate the program

serverName = 'localhost'
# Assign a port number
if(sys.argv > 4):

    try:
        serverPort = int(sys.argv[1])
        board_width = int(sys.arv[2])
        board_height = int(sys.argv[3])
        color = sys.argv[4:]


    except:
        printf("fail to get one of the values")

# Bind the socket to server address and server port
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))
sentence = input(' Input lower case sentence: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)

print('From server: ', modifiedSentence.decode())
clientSocket.close()
