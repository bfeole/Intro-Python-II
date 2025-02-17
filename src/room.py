# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, desc, items=[]):
        self.name = name
        self.desc = desc
        self.items = items

    def roomName(self):
        return self.name

    def roomDesc(self):
        return self.desc

    def getItems(self):
        return self.items

    def __str__(self):
        return self.name
