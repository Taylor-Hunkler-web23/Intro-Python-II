from room import Room
from player import Player
from item import Item



#Items
item = {
    'map':  Item("\nMap", "In this room there is a map."),
    'flashlight':  Item("\nFlashlight", "In this room there is a flashlight")
}

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

room['foyer'].roomitems = ['map']
room['narrow'].roomitems =['flashlight']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input("\nWhat is your name? "), room["outside"])

print(f"Welcome, {player.name}. Your are on a journey, searching for a lost treasure. Good luck!")
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


# def player_controls(user_pick):

    
#     # if user_pick.split(" ")[0] == "get":
#     #     player.get_item(user_pick.split(" ")[1])
     

#     # elif user_pick.split(" ")[0] == "drop":
#     #     player.drop_item(user_pick.split(" ")[1])
#     #     print(player.playeritems)
       

#     if user_pick == "search":
#         if len(player.room.roomitems) == 0:
#             print("Room has no items")
#         else:
#             new_item = input("what item would you like?")
#             player.get_item(new_item)
#             print(f"Your current items are {player.playeritems}")
            

#     elif user_pick == "drop":
#         if len(player.playeritems) == 0:
#             print("No items to drop")
#         else:
#             drop_item = input("what item would you drop?")
#             print(f"Your current items are {player.playeritems}")
#             player.drop_item(drop_item)
#             print(player.playeritems)

#     elif user_pick == "walk":
#         while True:
#             user_input = input("\n[n] to move North  [s] to move South   [e] to move East [w] to move West [q] to change action\nInput:")


#             if user_input == "q":
#                 print("you quit")
#                 break

#             elif user_input in directions:
#                 player.movement(user_input)
#                 print(f"\nYou have entered the {player.room.name}")
#                 print(player.room.description)
#                 print(player.room.roomitems)

           

#             elif not user_input in directions:
#                 print("Please enter valid input")

#     else:
#         print("Invalid input")










user_pick=""
# Write a loop that
while not quit:
    
    # Prints the current room name
    print(player.room)
    



#  Waits for user input and decides what to do.
    # print("\nChoose your next move: Type[search] to search room. Type [walk]To explore. Type [drop] To drop item.  [q] Quit\n Input:")

    user_pick =  input("\n Choose your next move. [n] to move North  [s] to move South   [e] to move East [w] to move West\nto get drop room items [get item] [drop item]\nInput:")

# If the user enters "q", quit the game.
    if user_pick == "q":
        quit = True
        print("you quit")

    # user_input = input("\n[n] to move North  [s] to move South   [e] to move East [w] to move West [q] to change action\nInput:")


        

    elif user_pick in directions:
        player.movement(user_pick)
        print(f"\nYou have entered the {player.room.name}")
        print(player.room.description)
        print(player.room.roomitems)


      
    elif user_pick.split(" ")[0] == "get":
        player.get_item(user_pick.split(" ")[1])
     

    elif user_pick.split(" ")[0] == "drop":
        player.drop_item(user_pick.split(" ")[1])
        print(player.playeritems)

    elif user_pick == "i":
        print(f"Current items you have: {player.playeritems}")


        

    else:
        print("Invalid input")
        

    # Print an error message if the movement isn't allowed.
    # elif not user_input in directions:
    #     print("Please enter valid input")

        
# If the user enters a cardinal direction, attempt to move to the room there.
    # elif user_input in directions:
    #     player.movement(user_input)

    
        


        
    

   