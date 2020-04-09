from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

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
newplayer = Player(room['outside'])

while not Player.move() == "q":
    print(newplayer.current_room.name)
    print(newplayer.current_room.description)
    if newplayer.current_room == room['outside']:
        if Player.move() == "n":
            newplayer = Player(room['foyer'])
            print(newplayer.current_room.name)
            print(newplayer.current_room.description)
        else:
            print('There is nothing but dence forest in that direction...')
    elif newplayer.current_room == room['foyer']:   
        if Player.move() == "n":
            newplayer = Player(room['overlook'])
            print(newplayer.current_room.name)
            print(newplayer.current_room.description)
        elif Player.move() == "s":
            newplayer = Player(room['outside'])
            print(newplayer.current_room.name)
            print(newplayer.current_room.description)
        elif Player.move() == "e":
            newplayer = Player(room['narrow'])
            print(newplayer.current_room.name)
            print(newplayer.current_room.description)
        else:
            print('There is nothing but a rocky cave wall in that direction...')
    elif newplayer.current_room == room['overlook']: 
        if Player.move() == "s":
            newplayer = Player(room['foyer'])
            print(newplayer.current_room.name)
            print(newplayer.current_room.description)
        else:
            print('There is nothing but a shear cliff there...')
    elif newplayer.current_room == room['narrow']: 
        if Player.move() == "w":
            newplayer = Player(room['foyer'])
            print(newplayer.current_room.name)
            print(newplayer.current_room.description)
        elif Player.move() == "n":
            newplayer = Player(room['treasure'])
            print(newplayer.current_room.name)
            print(newplayer.current_room.description)
        else:
            print('There is no passage through the walls smooth surface...')
    elif newplayer.current_room == room['treasure']: 
        if Player.move() == "s":
            newplayer = Player(room['narrow'])
            print(newplayer.current_room.name)
            print(newplayer.current_room.description)
        else:
            print('There is no passage through the walls smooth surface...')
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
