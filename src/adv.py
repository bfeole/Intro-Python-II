from room import Room
from player import Player
import os

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons a torch lays at your feet...", ["torch", ]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! A purse of gold coins sits in front of you. The only exit is to the south.""", ["coins", ]),
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

# Logic Controller

end = 0

# Character Creation

player_name = input('Whats your name? ')
player_age = input('How old are you? ')
player_spec = input('What kind of adventurer are you? ')

player_one = Player(player_name, player_age, player_spec, room['outside'])

# Instructions
print(' ')
print('|     -- "A Bards Tale" --     ')
print('|     -- ~~~~~~~~~~~~~~~ --     ')
print('|     -- < CONTROLS > --    ')
print('|     -- Move between rooms by typing [n]/[s]/[e]/[w]')
print('|     -- n = North / s = South / e = East / w = West')
print('|     -- Take items from the room by typing ["take item"] ')
print(
    '|     -- Leave items you have with you in the room by typing ["leave item"] ')
print('|     -- Press "q" to quit')


while not end:
    # Interface
    print(' ')
    print('|     -- < PLAYER ONE > --     ')
    print('|     -- ~~~~~~~~~~~~~~~ --     ')
    print(f'|     -- Name: {player_one.name} --     ')
    print(f'|     -- Age: {player_one.age} --     ')
    print(f'|     -- Class: {player_one.spec} --     ')
    print('|     -- ~~~~~~~~~~~~~~~ --     ')

    print('|     -- < LOCATION > --     ')
    print(f'|  -- {player_one.room.name} -- ')
    print(f'|  -- {player_one.room.desc} -- ')
    print('|     -- ~~~~~~~~~~~~~~~ --     ')

    print('|     -- < ROOM ITEMS > --     ')
    print(f'|        {str(player_one.room.items)}')
    print('|     -- ~~~~~~~~~~~~~~~ --     ')

    print('|     -- < INVENTORY > --     ')
    print(f'|        {player_one.items}')
    print('|     -- ~~~~~~~~~~~~~~~ --     ')
    print(' ')

# User Input
    movement = input('| >> What will you do? >> ')


# Game Logic
    if movement == 'q':
        end = 1

    if movement == 'take item':
        os.system('cls||clear')
        try:
            player_one.take_item(
                player_one.room.items[0]
            )
            print(
                f'| >> You pick up the {player_one.items[len(player_one.items) - 1]} and place it in your inventory <<')
        except:
            print('The room is empty')
    if movement == 'leave item':
        os.system('cls||clear')
        try:
            player_one.leave_item(
                player_one.items[0]
            )
        except:
            print('You are not caryying anything')

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

    # if len(movement) == 1 and movement != ['q', 'n', 's', 'w', 'e']:
    #     os.system('cls||clear')
    #     print('Please enter "n" "s" "w" "e" or "q" to quit')

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
