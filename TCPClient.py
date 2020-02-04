
# Import socket module
from socket import *

import sys # In order to terminate the program

#variables
i = 0


# Bind the socket to server address and server port
clientSocket = socket(AF_INET, SOCK_STREAM)

def post(board_width,board_height,colors):

    good_input = 0

    #validate note
    while good_input == 0:

        #ask user for note

        try:
            print("\n--Enter note to be posted ex - 'POST 2 3 10 20 white Meeting next Wednesday from 2 to 3--\n")
            note = input("Enter Note : ")
            correct_input = note.split(" ")

            if len(correct_input) >= 4:

                #this is to make sure the note itself is within the board defined
                width = int(correct_input[1]) + int(correct_input[3])
                height = int(correct_input[2]) + int(correct_input[4])

                color = correct_input[5]

                check_input = color in colors and correct_input[0] == "POST" and width <= int(board_width) and height <= int(board_height)
                print("POST COLOR IN COLORS:", color in colors)
                if(check_input):
                    good_input = 1
                    return note

        except:
            print("Incorrect input , try again..")
def getCoords(x,y):
    
    coordinates = ""
    coords = []

    good_input = 0
    
    while good_input == 0:

        try:

            while ((len(coordinates) < 3)):
                coordinates = input("Enter the coordinates,please make them comma seperated like this: <9 9>: ")
                coords = coordinates.split(" ")

                if (int(coords[0]) >= 0 and int(coords[0]) < int(x)):
                    if(int(coords[1]) >= 0 and int(coords[1]) < int(y)):
                        good_input = 1
                coords = list(coordinates.split(" "))
        except error as e:
            print(e.strerror)
            print("try again, bad input")


    
    return coords
def get(width, height):

    message = "GET "

    valid = 0
    In = ""
    yesNo = input("Would you like to set a color parameter? (y/n)\n")

    if yesNo == "y":
        In = input("Enter a color: ")
        message += "color="
        message += In
    
    valid = 0
    In = ""
    yesNo = input("Would you like to set a coordinate parameter? (y/n)\n")
    try:
        while (valid == 0 and yesNo == "y"):
            print("Enter the coordinates within the limits of the board")
            In = input("E.g: 9 8\n")
            if(int(In.split(" ")[0]) > 0 and  int(In.split(" ")[0]) < int(width) ):
                if(int(In.split(" ")[1]) > 0 and  int(In.split(" ")[1]) < int(width) ):
                    valid = 1
    except:
        pass

    if(yesNo == "y"):
        message += " contains= "
        message += In

    valid = 0
    In = ""
    yesNo = input("Would you like to set a refersTo parameter? (y/n)\n")

    if yesNo == "y":
        In = input("Enter a string: ")
        message += " refersTo="
        message += In
    
    print("Message at the end of the get function in client:\n", message)
    
        
    return message

    


counter = 0
disconnect = 0

while disconnect == 0:
    # print("Itetaration number",counter)
    counter += 1


    print("\n-----------------OPTIONS-------------\n")
    print("1. CONNECT\n")
    print("2. DISCONNECT\n")
    print("3. POST\n")
    print("4. GET\n")
    print("5. PIN\n")
    print("6. UNPIN\n")
    print("7. CLEAR\n")

    print("\n---USE NUMBERS TO PICK OPTION---\n")


    good_input = 0
    option = 0

    #validate an actual option is chosen
    while good_input == 0:
     
        option = int(input("Enter Option (1-7): "))
    
        if(option >= 1 and option <= 7):
            good_input = 1

    #keep trying if it doesnt work
    print("Before connecting")

    try:
        print("INSIDE TRY STATEMENT")

        #check which options and respond accordingly
        if option == 1:
            serverPort = int(input("Server port: "))
            serverAddr = input("Server address: ")
            
            clientSocket.connect((serverAddr, serverPort))

            #grabs info needed to to client functions
            formattedMessage = clientSocket.recv(1024)
            print('From server: ', formattedMessage.decode())
            formattedMessage = formattedMessage.decode().split(" ")

            #get values of board
            board_width = formattedMessage[1]
            board_height = formattedMessage[2]
            colors = formattedMessage[3:]

        elif option == 2:
            message = "2 "
            #send message with option
            clientSocket.send(message.encode())
            modifiedSentence = clientSocket.recv(1024)
            
            clientSocket.close()
            disconnect = 1  

        elif option == 3:

            
            note = post(board_width,board_height,colors)
            message = "3 " + note
            #send message with note and option dictated
            clientSocket.send(message.encode())
        
        elif option == 4:

            color = ""
            coordinates = []
            refersTo = ""

            message = get(board_width,board_height)
            message = "4 " + message

            #send message with note and option dictated
            clientSocket.send(message.encode())

        elif option == 5:
            coords = getCoords(board_width, board_height)
            message = "5 " + coords[0] + " " + coords[1]
            print("message",message)
            clientSocket.send(message.encode())
        elif option == 6:
            coords = getCoords(board_width, board_height)
            message = "6 " + coords[0] + " " + coords[1]
            print("message",message)
            clientSocket.send(message.encode())

        elif option == 7:


            message = "7 "
            
            #send message with note and option dictated
            clientSocket.send(message.encode())
            
    except error as e: 
        print(e.strerror)
        print("error try connecting before starting any process..")




