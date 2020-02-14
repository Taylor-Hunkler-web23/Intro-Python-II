from room import Room
from player import Player
from item import Item



#Items
item = {
    'map':  Item("\nMap", "In this room there is a map."),
    'flashlight':  Item("\nFlashlight", "In this room there is a flashlight")
}

map = Item("map", "You found a map")
# Declare all the rooms

room = {
    'outside':  Room("\nOutside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
# room['foyer'] = {map.description}




# Link rooms with items

room['foyer'].items = ['map']
room['narrow'].items =['flashlight']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input("What is your name?"), room["outside"])

print(f"Welcome, {player.name}")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

quit = False
directions = "nsew"


def player_controls(user_pick):

    if user_pick == "search":
        if len(player.room.items) == 0:
            print("Room has no items")
        else:
            new_item = input("what item would you like?")
            player.get_item(new_item)
            print(player.room.items)

    elif user_pick == "drop":
        if len(player.playeritems) == 0:
            print("No items to drop")
        else:
            drop_item = input("what item would you drop?")
            print("Your current items are {player.playeritems}")
            player.drop_item(drop_item)
            print(player.playeritems)

    elif user_pick == "walk":
        while True:
            user_input = input("[n] North  [s] South   [e] East [w] West [q] change action\nInput:")


            if user_input == "q":
                print("you quit")
                break

            elif user_input in directions:
                player.movement(user_input)
                print(player.room)

           

            elif not user_input in directions:
                print("Please enter valid input")










user_pick=""
# Write a loop that
while not quit:
    
    # Prints the current room name
    print(player.room)
    



#  Waits for user input and decides what to do.
    print("Choose your next move: [search] to search room. [walk]To explore. [drop] To drop item.  [q] Quit\nInput:")

    user_pick = input("")

# If the user enters "q", quit the game.
    if user_pick == "q":
        quit = True
        print("you quit")

        

    else:
        player_controls(user_pick)
        

    # Print an error message if the movement isn't allowed.
    # elif not user_input in directions:
    #     print("Please enter valid input")

        
# If the user enters a cardinal direction, attempt to move to the room there.
    # elif user_input in directions:
    #     player.movement(user_input)

    
        


        
    

   