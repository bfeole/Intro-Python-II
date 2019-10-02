from room import Room
from player import Player
import os

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

end = 0

player_name = input('Whats your name? ')
player_age = input('How old are you? ')
player_spec = input('What kind of adventurer are you? ')

player_one = Player(player_name, player_age, player_spec, room['outside'])

# player_one = Player("Kovthe", 22, "Bard", room['outside'], )

print('Move between rooms by typing n/s/e/w')
print('n = North / s = South / e = East / w = West')
print('Press "q" to quit')

while not end:
    print(player_one.room.name)
    print(player_one.room.desc)

    # print(room[player_one.currentRoom].roomDesc())
    # print(room[player_one.currentRoom].n_to)

    movement = input('Which way would you like to go? >> ')

    if movement == 'q':
        end = 1
    if movement == 'n':
        os.system('cls||clear')
        try:
            player_one.changeRoom(
                player_one.room.n_to)
        except:
            print('Please try again')
    if movement == 's':
        os.system('cls||clear')
        try:
            player_one.changeRoom(
                player_one.room.s_to)
        except:
            print('Please try again')
    if movement == 'w':
        os.system('cls||clear')
        try:
            player_one.changeRoom(
                player_one.room.w_to)
        except:
            print('Please try again')
    if movement == 'e':
        os.system('cls||clear')
        try:
            player_one.changeRoom(
                player_one.room.e_to)
        except:
            print('Please try again')

        # while True:
        #     print(f"{player_one.room.name}")
        #     print(f"{player_one.room.desc}")

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
