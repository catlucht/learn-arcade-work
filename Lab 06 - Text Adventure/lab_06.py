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


def main():
    room_list = []

    # Bedroom (Room 0)
    room = Room(
                "You are in a bedroom. It is dark and dusty. \nAll the windows are boarded shut. "
                "There is a door to the east.",
                None,
                None,
                1,
                None)
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
            None,
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

    current_room = 0

    done = False
    while not done:
        print()
        print(room_list[current_room].description)
        action = input("In which direction would you like to go? ")

        # Moving north
        if action.lower() == "n" or action.lower() == "north":
            next_room = room_list[current_room].north

            if next_room is None:
                print()
                print("You can't go that way.")

            else:
                current_room = next_room

        # Moving south
        elif action.lower() == "s" or action.lower() == "south":
            next_room = room_list[current_room].south

            if next_room is None:
                print()
                print("You can't walk through walls.")

            else:
                current_room = next_room

        # Moving west
        elif action.lower() == "w" or action.lower() == "west":
            next_room = room_list[current_room].west

            if next_room is None:
                print()
                print("There is no where to go that way.")

            else:
                current_room = next_room

        # Moving east
        elif action.lower() == "e" or action.lower() == "east":
            next_room = room_list[current_room].east

            if next_room is None:
                print()
                print("You can't go that way.")

            else:
                current_room = next_room

        # Quit action
        elif action.lower() == "q" or action.lower() == "quit":
            print()
            print("Goodbye.")
            done = True

        # Unknown input
        else:
            print()
            print("You can only go north, south, east, or west.")


main()
