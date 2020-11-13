class Room:
    """
    This is the class for the room
    """
    def __init__(self, description, north, south, east, west, up, down):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down


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
                "You are in a bedroom. It is dark and dusty.\nAll the windows are boarded shut. "
                "You don't know how you got here...\n"
                "There are doors to the east and west.",
                None,
                None,
                1,
                7,
                None,
                None)
    room_list.append(room)

    # Hall (Room 1)
    room = Room(
                "You are in a hallway. There are portraits hanging on the walls. "
                "\nThe eyes seem to follow you as you move. Doors surround you to the north, south, and west."
                "\nYou can also go down the stairs.",
                3,
                4,
                None,
                0,
                None,
                2)
    room_list.append(room)

    # Basement (Room 2)
    room = Room(
            "You are in a dark basement. The only exit you see is up the stairs.",
            None,
            6,
            None,
            None,
            1,
            None)
    room_list.append(room)

    # Garden (Room 3)
    room = Room(
            "You are in a garden of dead and rotted plants. \nThere is a door to the south.",
            None,
            1,
            None,
            None,
            None,
            None)
    room_list.append(room)

    # Living room (Room 4)
    room = Room(
            "You are in a living room. The television only tunes to static. The phone wire has been cut... "
            "\nAbove the landline you can make out the number 406-758-9031."
            "\nThere are doors to the north and south.",
            1,
            5,
            None,
            None,
            None,
            None)
    room_list.append(room)

    # Kitchen (Room 5)
    room = Room(
            "You are in a kitchen. There is a door to the north.",
            4,
            None,
            None,
            None,
            None,
            None)
    room_list.append(room)

    # Hidden Room (Room 6)
    room = Room(
            "You are in a hidden room. There is a door to the north.",
            2,
            None,
            None,
            None,
            None,
            None)
    room_list.append(room)

    # Closet (Room 7)
    room = Room(
            "You are in a dark closet. There is a door to the east.",
            None,
            None,
            0,
            None,
            None,
            None)
    room_list.append(room)

    current_room = 0

    # Journal (Bedroom 0)
    journal = Item(0, "journal", "There is an old leather bound journal. There is a page sticking out...")
    item_list.append(journal)

    # Key (Closet 7)
    key = Item(7, "key", "You see a little silver key.")
    item_list.append(key)

    # Flashlight (Closet 7)
    flashlight = Item(7, "flashlight", "There is a powerful flashlight. That might be useful later...")
    item_list.append(flashlight)

    # Notepad (Closet 7)
    notepad = Item(7, "notepad", "You see a notepad. There is some writing on it.")
    item_list.append(notepad)

    # Sheers (Garden 3)
    sheers = Item(3, "sheers", "There is a pair of sheers.")
    item_list.append(sheers)

    # Bone (Kitchen 5)
    bone = Item(5, "bone", "There is a large bone on the table. Gross...")
    item_list.append(bone)

    # Door knob (Hidden room 6)
    door_knob = Item(6, "door knob", "You spot a shiny brass door knob. Have you seen a door without a knob?...")
    item_list.append(door_knob)

    done = False
    while not done:
        print()

        # Print room description
        print(room_list[current_room].description)

        # print items in current room
        for item in item_list:
            if item.room == current_room:
                print(item.description)

        # User action input
        action = input("What would you like to do? ")
        command_words = action.split(" ")

        # Moving north
        if action.lower() == "n" or action.lower() == "north" or action.lower() == "move north" \
                or action.lower() == "go north" or action.lower() == "walk north":

            next_room = room_list[current_room].north

            if next_room is None:
                print()
                print("You can't go that way.")

            else:
                current_room = next_room

        # Moving south
        elif action.lower() == "s" or action.lower() == "south" or action.lower() == "move south" \
                or action.lower() == "go south" or action.lower() == "walk south":
            next_room = room_list[current_room].south

            if next_room is None:
                print()
                print("You can't walk through walls.")

            else:
                current_room = next_room

        # Moving west
        elif action.lower() == "w" or action.lower() == "west" or action.lower() == "move west" \
                or action.lower() == "go west" or action.lower() == "walk west":

            next_room = room_list[current_room].west

            if next_room is None:
                print()
                print("There is no where to go that way.")

            else:
                current_room = next_room

        # Moving east
        elif action.lower() == "e" or action.lower() == "east" or action.lower() == "move east" \
                or action.lower() == "go east" or action.lower() == "walk east":

            next_room = room_list[current_room].east

            if next_room is None:
                print()
                print("You can't go that way.")

            else:
                current_room = next_room

        # Moving up
        elif action.lower() == "up" or action.lower() == "upstairs":
            next_room = room_list[current_room].up

            if next_room is None:
                print()
                print("Walking that way isn't helpful.")

            else:
                current_room = next_room

        # Moving down
        elif action.lower() == "down" or action.lower() == "downstairs":
            next_room = room_list[current_room].down

            if next_room is None:
                print()
                print("There is no where to go that way.")

            else:
                current_room = next_room

        # # Using journal
        # elif action.lower() == "read journal" or action.lower() == "read page":
        #     print()
        #     print("\"... this house always gave me the creeps. I knew something was off about it. "
        #             "\n It feels like this house is alive... I don't even remember anymore how I got here. "
        #             "\n I miss my family... At least I think I have a family. I don't remember anymore."
        #             "\n I think I am going to try and escape. Wish me luck, journal...\"")
        #
        # # Using shoe box
        # elif action.lower() == "open shoe box" or action.lower() == "shoe box":
        #     print()
        #     print("Inside the shoe box you find a note.")
        #
        # elif action.lower() == "read note" or action.lower() == "note":
        #     print()
        #     print("\"A1 B2 C3 D4 E5 F6 G7 H8 I9 J10 K11 L12 M13 N14 O15"
        #             "\nP16 Q17 R18 S19 T20 U21 V22 W23 X24 Y25 Z26\"")

        # Quit action
        elif action.lower() == "q" or action.lower() == "quit":
            print()
            print("Goodbye.")
            done = True

        elif action.lower() == "inventory" or action.lower() == "check inventory":
            print()
            print("Inventory:")
            for item in item_list:
                if item.room == -1:
                    print(item.name)

        elif command_words[0].lower() == "get":
            picked_up = False
            for item in item_list:
                if command_words[1].lower() == item.name and item.room == current_room:
                    item.room = -1
                    print()
                    print("You have picked up", item.name)
                    picked_up = True
            if not picked_up:
                print()
                print("That item doesn't seem to be here")

        elif command_words[0].lower() == "drop":
            dropped = False
            for item in item_list:
                if command_words[1].lower() == item.name and item.room == -1:
                    item.room = current_room
                    print()
                    print("You dropped", item.name)
                    dropped = True
            if not dropped:
                print()
                print("You don't have that item.")

        # Unknown input
        else:
            print()
            print("That is an invalid command.")


main()
