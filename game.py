import random

#PLAYER

#COMPUTER

#MAP
psw_player = [] #Saves the positions where the ship is for the player map
psw_computer = [] #Saves the positions where the ship is for the computer map

def generateEmptyMap(): #We create an empty map
    my_map = []
    for i in range(10):#To create each row
        new_list = [] #creating an empty list each time
        for j in range(10):
            new_list.append(" - ") #Adding the elements
        my_map.append(new_list) #Adding the row to the map
    return my_map


def addShipstoMap(my_map, size, number_of_ships, pws):
    for i in range(number_of_ships): #To creating as many ships we want
        n1 = random.randint(0, 9)
        n2 = random.randint(0, 9)
        direction = random.randint(0, 1) #0 for up, 1 for right
        my_map[n1][n2] = " * " #adding the first ship box
        for j in range(size-1): #Adding ship size next to the selected box
            pass #we need to check the direction of the ship, and make an exception for indexoutofrange, and it this happens, we eliminate the added box ships and we try it again in the other direction, 
                #but in case that it finds another pws in the way we choose again another ship box randomnly. This until
                #we had placed all the ships

    


def printAllMap(my_map): #We print any map that we pass it in the correct format
    for i in range(10):#Acces the specific row
        for j in my_map[i]: #Acces each element of the row
            print(j, end="") #Print it without passing next line
        print("") #Line jump


player_map = generateEmptyMap()
printAllMap(player_map)