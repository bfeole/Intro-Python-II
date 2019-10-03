# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, age, spec, room, items=[]):
        self.name = name
        self.age = age
        self.spec = spec
        self.room = room
        self.items = items

    def currentRoom(self):
        return self.room

    def changeRoom(self, room):
        self.room = room

    def take_item(self, item):
        self.items.append(item)
        self.room.items.remove(item)

    def leave_item(self, item):
        self.items.remove(item)
        self.room.items.append(item)

    def __str__(self):
        return 'Name: ' + self.name + ' Age: ' + self.age + ' Specialization: ' + self.spec
