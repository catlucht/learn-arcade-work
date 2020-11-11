class Room:
    """
    This is the class for the room
    """
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


class Item:
    def __init__(self, room, name, description):
        self.room = room
        self.name = name
        self.description = description


class Player:
    pass
    # def pickup(self, room, item):
    #     room.items.remove(item)
    #     self.inventory.append(item)

    def examine(self, room):
        pass


def main():
    room_list = []
    item_list = []

    # Bedroom (Room 0)
    room = Room(
                "You are in a bedroom. It is dark and dusty. \nAll the windows are boarded shut. "
                "You don't know how you got here... "
                "\nLooking around the room you see a bed, a dresser, and a bookshelf. "
                "\nThere are doors to the east and west.",
                None,
                None,
                1,
                8)
    room_list.append(room)

    # Hall (Room 1)
    room = Room(
                "You are in a hallway. There are portraits hanging on the walls. "
                "\nThe eyes seem to follow you as you move. Doors surround you in all directions.",
                4,
                5,
                2,
                0)
    room_list.append(room)

    # Stairs (Room 2)
    room = Room(
            "You are in a stairwell. Every other step is missing... \nThere are doors to the east and west.",
            None,
            None,
            3,
            1)
    room_list.append(room)

    # Basement (Room 3)
    room = Room(
            "You are in a dark basement. There is a door to the west.",
            None,
            7,
            None,
            2)
    room_list.append(room)

    # Garden (Room 4)
    room = Room(
            "You are in a garden of dead and rotted plants. \nThere is a door to the south.",
            None,
            1,
            None,
            None)
    room_list.append(room)

    # Living room (Room 5)
    room = Room(
            "You are in a living room. The television only tunes to static. The phone wire has been cut... "
            "\nThere are doors to the north and south.",
            1,
            6,
            None,
            None)
    room_list.append(room)

    # Kitchen (Room 6)
    room = Room(
            "You are in a kitchen. You already checked, all the food is expired and moldy. "
            "\nThere is a door to the north.",
            5,
            None,
            None,
            None)
    room_list.append(room)

    # Hidden Room (Room 7)
    room = Room(
            "You are in a hidden room.",
            3,
            None,
            None,
            None)
    room_list.append(room)

    # Closet (Room 8)
    room = Room(
            "You are in a dark closet. Feeling around, you find a shoe box, a key, a flash light, and a notepad. "
            "The exit is to the east.",
            None,
            None,
            0,
            None)
    room_list.append(room)

    current_room = 0

    # Journal (Bedroom 0)
    journal = Item(0, "journal", "An old leather bound journal. There is a page sticking out...")
    item_list.append(journal)

    # Key (Closet 8)
    key = Item(8, "key", "A little silver key.")
    item_list.append(key)

    # Flashlight (Closet 8)
    flashlight = Item(8, "flashlight", "A powerful flashlight. This might be useful in a dark room...")
    item_list.append(flashlight)

    done = False
    while not done:
        print()

        print(room_list[current_room].description)
        action = input("What is your command? ")

        # Moving north
        if action.lower() == "go north" or action.lower() == "north" or action.lower() == "move north":
            next_room = room_list[current_room].north

            if next_room is None:
                print()
                print("You can't go that way.")

            else:
                current_room = next_room

        # Moving south
        elif action.lower() == "go south" or action.lower() == "south" or action.lower() == "move south":
            next_room = room_list[current_room].south

            if next_room is None:
                print()
                print("You can't walk through walls.")

            else:
                current_room = next_room

        # Moving west
        elif action.lower() == "go west" or action.lower() == "west" or action.lower() == "move west":
            next_room = room_list[current_room].west

            if next_room is None:
                print()
                print("There is no where to go that way.")

            else:
                current_room = next_room

        # Moving east
        elif action.lower() == "go east" or action.lower() == "east" or action.lower() == "move east":
            next_room = room_list[current_room].east

            if next_room is None:
                print()
                print("You can't go that way.")

            else:
                current_room = next_room

        # Bedroom Bed
        elif action.lower() == "go to bed" or action.lower() == "bed":
            print()
            print("The bed doesn't look like it's been slept in in years. There is a journal on the pillow.")

        # Bedroom Dresser
        elif action.lower() == "go to dresser" or action.lower() == "dresser":
            print()
            print("The dresser is very dusty. All the drawers are empty.")

        # Bedroom Bookshelf
        elif action.lower() == "go to bookshelf" or action.lower() == "bookshelf":
            print()
            print("This doesn't seem like the time for free-reading...")

        # Using journal
        elif action.lower() == "read journal" or action.lower() == "read page":
            print()
            print("\"... this house always gave me the creeps. I knew something was off about it. "
                    "\n It feels like this house is alive... I don't even remember anymore how I got here. "
                    "\n I miss my family... At least I think I have a family. I don't remember anymore."
                    "\n I think I am going to try and escape. Wish me luck, journal...\"")

        # Using shoe box
        elif action.lower() == "open shoe box" or action.lower() == "shoe box":
            print()
            print("Inside the shoe box you find a note.")

        elif action.lower() == "read note" or action.lower() == "note":
            print()
            print("\"A1 B2 C3 D4 E5 F6 G7 H8 I9 J10 K11 L12 M13 N14 O15"
                    "\nP16 Q17 R18 S19 T20 U21 V22 W23 X24 Y25 Z26\"")

        # Quit action
        elif action.lower() == "q" or action.lower() == "quit":
            print()
            print("Goodbye.")
            done = True

        # Unknown input
        else:
            print()
            print("That is an invalid command.")


main()
