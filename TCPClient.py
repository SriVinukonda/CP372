
# Import socket module
from socket import *

import sys # In order to terminate the program

#variables
i = 0


# Bind the socket to server address and server port
clientSocket = socket(AF_INET, SOCK_STREAM)

def post(board_width,board_height):

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

                check_input = correct_input[0] == "POST" and width <= int(board_width) and height <= int(board_height)

                if(check_input):
                    good_input = 1
                    return note

        except:
            print("Incorrect input , try again..")

def get_pins(color,coordinates,refersTo):
    
    print("\n--------general format--------\n")
    print("color = <color> contains = <coord> refersTo = <string>\n")
    print("partial gets is allowed however format above needs to be followed\n")
   
    #error handling still needed
    good_input = False

    get_pins = input("Enter the pins wanted/needed: ")

    return get_pins

    check_input = get_pins.split(" ,")

def pin():
    
    coordinates = ""
    coords = []

    while ((len(coordinates) < 3)):
        coordinates = input("Enter the coordinates,please make them comma seperated like this: <9 9>: ")
        if(coordinates == " "):
            break;
        coords = list(coordinates.split(" "))


    
    return coords

counter = 0
disconnect = 0

while disconnect == 0:
    print("Itetaration number",counter)
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

        elif option == 2:
            message = "2 "
            #send message with option
            clientSocket.send(message.encode())
            clientSocket.close()
            disconnect = 1  

        elif option == 3:

            
            note = post(board_width,board_height)
            message = "3 " + note
            #send message with note and option dictated
            clientSocket.send(message.encode())
        
        elif option == 4:

            color = ""
            coordinates = []
            refersTo = ""

            pins = get_pins(color,coordinates,refersTo)

            message = "4 " + pins

            #send message with note and option dictated
            clientSocket.send(message.encode())

        elif option == 5:
            coords = pin()
            message = "5 " + coords[0] + " " + coords[1]
            print("message",message)
            clientSocket.send(message.encode())

        elif option == 7:


            message = "7 "
            
            #send message with note and option dictated
            clientSocket.send(message.encode())
            
    except error as e: 
        print(e.strerror)
        print("error try connecting before starting any process..")




