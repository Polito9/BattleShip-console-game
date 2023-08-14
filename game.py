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


def validatePosition(x, y, map, psw): #Add the case if it is computer or player
    mini_list = [x, y]
    if (mini_list in psw): #Verifico que la posición indicada sea una de un barco
        print("Acertaste!")
        map[int(x)][int(y)] = " X "
        psw.remove(mini_list)
    else:
        print("Lo siento, fallaste")
        map[int(x)][int(y)] = " O " #cambio la variable


def playPlayer_sTurn(): #Plays all the steps of the players turn
    global psw_computer
    global computer_map
    x = int(input("Ingresa tu coordenada y: "))
    y = int(input("Ingresa su coordenada x: "))
    validatePosition(x, y, computer_map, psw_computer)

def playComputer_sTurn(): #Plays and checks everything for making a good computer turn
    #if there is no hint
    global psw_computer
    global player_map
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    validatePosition(x, y, player_map, psw_player)

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
print(psw_computer)
print("This is your game:")
printAllMap(player_map)
#Specify that cordinates start ar superior corner left. 
while not gameFinished:
    while len(psw_computer) > 0 or len(psw_player) > 0:
        playPlayer_sTurn()
        printCensoredMap(computer_map)
        print("______________________________________")
        #Turno de la computadora

    else:
        print("JUEGO TERMINADO, ESTOS SON LOS RESULTADOS: ")

