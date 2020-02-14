# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.playeritems = []

    def movement(self, direction):
        new_room = self.room.go_to_room(direction)
        if new_room is not None:
            self.room = new_room
            
        else:
            print("No room there, try again")

    def get_item(self, new_item):
        if new_item in self.room.roomitems:
            print(f"You got {new_item}")
            self.playeritems.append(new_item)
            self.room.roomitems.remove(new_item)
            print(f"you now have {self.playeritems}")
        else:
            print("There are no items with that name")


    def drop_item(self, item):
        if item in self.playeritems:
            print(f"You dropped {item}")
            self.playeritems.remove(item)
            self.room.roomitems.append(item)
            print(f"you now have {self.playeritems}")
        else:
            print("There are no items with that name")