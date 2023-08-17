import random
#MAP
psw_player = [] #Saves the positions where the ship is for the player map
psw_computer = [] #Saves the positions where the ship is for the computer map
player_map = []
computer_map = []
gameFinished = False
def generateEmptyMap(): #We create an empty map
    my_map = []
    for i in range(10):#To create each row
        new_list = [] #creating an empty list each time
        for j in range(10):
            new_list.append(" - ") #Adding the elements
        my_map.append(new_list) #Adding the row to the map
    return my_map

def deleteShipsFromMap(my_map, positions): 
    for pos in positions:
        row, col = pos
        if row < len(my_map) and col < len(my_map[row]):
            my_map[row][col] = " - "

def addShipstoMap(my_map, size, number_of_ships, pws):
    i = 0
    while i < number_of_ships: #To creating as many ships we want
        posible_positions_to_delete = []
        n1 = random.randint(0, 9)
        n2 = random.randint(0, 9)
        direction = random.randint(0, 1) #0 for up, 1 for right
        for j in range(size): #Adding ship size next to the selected box
            side = 1 #To could detect if the ship is gonna hit some wall, so we change this to change side to add boxes
            if direction == 0: #Check for up
                if (n2+size > 9): #Validates if it is going to pass the border
                    side = -1
                if ([n1,n2+(j*side)] in pws):
                    deleteShipsFromMap(my_map, posible_positions_to_delete)
                    i -= 1
                    break
                else:
                    pws.append([n1, n2+(j*side)])
                    my_map[n1][n2+(j*side)] = " * " #Add the boxes up
                    posible_positions_to_delete.append([n1, n2+(j*side)])
            else: #To going right
                if (n1+size > 9): #Changes direction to left if it is going to pass the border
                    side = -1
                if ([n1+(j*side),n2] in pws):
                    deleteShipsFromMap(my_map, posible_positions_to_delete)
                    i -= 1
                    break
                else:
                    pws.append([n1+(j*side), n2])
                    my_map[n1+(j*side)][n2] = " * "
                    posible_positions_to_delete.append([n1+(j*side), n2])
        i += 1#When we delete one, the counter keeps summing

#Printing maps
def printAllMap(my_map): #We print any map that we pass it in the correct format
    for i in range(10):#Acces the specific row
        for j in my_map[i]: #Acces each element of the row
            print(j, end="") #Print it without passing next line
        print("") #Line jump

def printCensoredMap(my_map): #We print any map that we pass it in the correct format
    for i in range(10):#Acces the specific row
        for j in my_map[i]: #Acces each element of the row
            if (j != " * "):
                print(j, end="") #Print it without passing next line
            else:
                print(" - ", end="") 
        print("") #Line jump

def validatePosition(x, y, map, psw, msg_c, msg_i): #Checks if the position is one in the pws
    mini_list = [x, y]
    if (mini_list in psw): #Verifico que la posición indicada sea una de un barco
        map[int(x)][int(y)] = " X "
        psw.remove(mini_list)
        print(msg_c)
    else:
        map[int(x)][int(y)] = " O " #cambio la variable
        print(msg_i)

def playPlayer_sTurn(): #Plays all the steps of the players turn
    global psw_computer
    global computer_map
    continue_game = False
    while not continue_game:
        y = int(input("Enter the x-coordinate: "))
        x = 9 - int(input("Enter the y-coordinate: "))
        continue_game = (x <= 9 and x >= 0) and (y <= 9 and y >= 0)
        if not continue_game:
            print("Valores ingresados no válidos, intentalo nuevamente\n\n")
    msg_c = "<<<<Congrats, you got it!>>>>"
    msg_i = "<<<<Sorry, you've failed>>>>"
    validatePosition(x, y, computer_map, psw_computer, msg_c, msg_i)
    print("_____________________________________\nCOMPUTER MAP: ")

def playComputer_sTurn(): #Plays and checks everything for making a good computer turn
    #if there is no hint
    global psw_computer
    global player_map
    #By random
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    msg_c = "The computer has hit"
    msg_i = "The computer failed"
    validatePosition(x, y, player_map, psw_player, msg_c, msg_i)
    print("_____________________________________\n YOUR MAP: ")
    printAllMap(player_map)

    #Validates if it has a hint, and selects one box according to that
    
def startGame():
    global player_map
    global computer_map
    #Player map
    player_map = generateEmptyMap()
    addShipstoMap(player_map, 3, 2, psw_player)
    addShipstoMap(player_map, 1, 3, psw_player)
    addShipstoMap(player_map, 2, 2, psw_player)
    #Computer map
    
    computer_map = generateEmptyMap()
    addShipstoMap(computer_map, 3, 2, psw_computer)
    addShipstoMap(computer_map, 1, 3, psw_computer)
    addShipstoMap(computer_map, 2, 2, psw_computer)

#Computers turn
startGame()
print("This is your map:")
printAllMap(player_map)
#Specify that cordinates start ar superior corner left. 
while not gameFinished:
    while len(psw_computer) > 0 and len(psw_player) > 0:
        input("\n\nIt's your turn. Enter to continue\n")
        playPlayer_sTurn()
        printCensoredMap(computer_map)
        #Turno de la computadora
        input("\n\nIt's computer's turn. Enter to continue\n")
        playComputer_sTurn()
        print("PSW_C SIZE: "+str(len(psw_computer)))
    else:
        print("GAME FINISHED, THERE ARE THE RESULTS: \n\n")
        if (len(psw_player) > 0):
            print("YOU HAVE WON THE GAME, CONGRATULATIONS!!!!!!\n\n")
        else:
            print("SORRY ): YOU HAVE LOSE AGAINST A MACHINE\n\n")
        gameFinished = True

print("------------------------------------------------")
print("Thanks for playing :)")
print("Author: Polito09\n")