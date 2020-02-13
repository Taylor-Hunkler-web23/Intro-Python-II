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
            print("Going to next room")
        else:
            print("No room there, try again")

    def get_item(self, item):
        if item in self.room.items:
            print(f"You got {item}")
            self.playeritems.append(item)
            self.room.items.remove(item)
            print(f"you now have {self.playeritems}")
        else:
            print("There are no items")

