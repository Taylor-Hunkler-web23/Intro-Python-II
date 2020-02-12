# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def movement(self, direction):
        new_room = self.room.go_to_room(direction)
        if new_room is not None:
            self.room = new_room
            print("Going to next room")
        else:
            print("Try again")
