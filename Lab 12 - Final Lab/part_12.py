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


def main():
    room_list = []
    item_list = []

    # Bedroom (Room 0)
    room = Room(
                "You are in a bedroom. It is dark and dusty.\nAll the windows are boarded shut. "
                "There are doors to the east and west. The door to the east seems to be locked...",
                None,
                None,
                None,
                7,
                None,
                None)
    room_list.append(room)

    # Hall (Room 1)
    room = Room(
                "You are in a hallway. There are portraits hanging on the walls. "
                "\nThe eyes seem to follow you as you move. Doors surround you to the north, south, and west."
                "\nThere is a lock on a door to go down to the basement.",
                3,
                4,
                None,
                0,
                None,
                None)
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
            "You are in a garden of dead and rotted plants. There is a large menacing dog barking at you."
            "\nHe seems to be guarding something... There is a door to the south.",
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
            "\nThere are doors to the north and south. The house's front door seems to be to the west."
            "\nIt's chained shut and missing the door knob... Maybe there's a different way out.",
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

    # Outside (Room 10)
    room = Room(
            "A strong breeze overwhelms you as you open the front door. The sun so bright, you have to squint to see"
            "\nBut you see it... freedom. You think of your parents, they have to be searching for you."
            "\nYou wonder what your friends have been up to since you've been gone. You miss them."
            "\nBut you have it, finally... freedom... sweet freedom...",
            None,
            None,
            None,
            None,
            None,
            None)

    current_room = 0

    # 0 Journal (Bedroom 0)
    journal = Item(0, "journal", "There is an old leather bound journal on the bed. There is a page sticking out...")
    item_list.append(journal)

    # 1 Shoebox (Bedroom 0)
    shoebox = Item(0, "shoebox", "There is a shoebox peaking out from under the bed.")
    item_list.append(shoebox)

    # 2 Key (Closet 7)
    key = Item(7, "key", "You see a little silver key.")
    item_list.append(key)

    # 3 Flashlight (Closet 7)
    flashlight = Item(7, "flashlight", "There is a powerful flashlight. That might be useful later...")
    item_list.append(flashlight)

    # 4 Notepad (Closet 7)
    notepad = Item(7, "notepad", "You see a notepad. There is some writing on it.")
    item_list.append(notepad)

    # 5 Bolt cutters (Garden 3)
    bolt_cutters = Item(None, "bolt cutters", "There are a pair of bolt cutters next to the dog.")
    item_list.append(bolt_cutters)

    # 6 Bone (Kitchen 5)
    bone = Item(5, "bone", "There is a large bone on the table. Gross...")
    item_list.append(bone)

    # 7 Door knob (Hidden room 6)
    door_knob = Item(6, "door knob", "You spot a shiny brass door knob. Have you seen a door without a knob?...")
    item_list.append(door_knob)

    done = False
    found_door_knob = False
    used_bolt_cutters = False

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

        # Using journal
        elif command_words[0].lower() == "read":
            if len(command_words) > 1:
                if item_list[0].room == -1:
                    if command_words[1].lower() == "journal" or command_words[1].lower() == "page":
                        print()
                        print("\"... this house always gave me the creeps. I knew something was off about it. "
                              "\n It feels like this house is alive... I don't even remember anymore how I got here. "
                              "\n I miss my family... At least I think I have a family. I don't remember anymore."
                              "\n I think I am going to try and escape. Wish me luck, journal...\"")
                if item_list[4].room == -1:
                    if command_words[1].lower() == "notepad":
                        print()
                        print("The only way out is to 'escape'")
                else:
                    print()
                    print("You can't read that.")
            else:
                print()
                print("Yes, we should all read.")

        # Using shoe box
        elif command_words[0] == "open":
            if len(command_words) > 1:
                if command_words[1] == "shoebox":
                    if item_list[1].room == -1:
                        print()
                        print("Inside the shoe box you find a note:"
                              "\nA1 B2 C3 D4 E5 F6 G7 H8 I9 J10 K11 L12 M13 N14 O15 "
                              "\nP16 Q17 R18 S19 T20 U21 V22 W23 X24 Y25 Z26")
                    else:
                        print()
                        print("You don't have that item.")
                else:
                    print()
                    print("That can't be opened.")
            else:
                print()
                print("What would you like to open?")

        # Bedroom door passcode
        elif command_words[0].lower() == "enter":
            if command_words[1] == "51931165":
                print()
                print("The door unlocked.")
                room_list[0].east = 1
                room_list[0].description = "You are in a bedroom. It is dark and dusty." \
                                           "\nAll the windows are boarded shut." \
                                           "\nThere are doors to the east and west."
            else:
                print()
                print("The door is still locked. That was the wrong code...")

        # Basement lock
        elif command_words[0].lower() == "use":
            if command_words[1] == "key":
                if item_list[2] == -1:
                    print()
                    print("The door is unlocked.")
                    room_list[1].down = 2

                else:
                    print()
                    print("You don't have the key for this door.")

        # Use door knob
        elif command_words[0].lower() == "use":
            if command_words[1].lower() == "door knob":
                print()
                print("The door knob is now in place")
                item_list[7].room = None
                found_door_knob = True

                if found_door_knob and used_bolt_cutters:
                    print()

                    room_list[4].west = 10

        # Pet dog
        elif command_words[0].lower() == "pet":
            if command_words[1].lower() == "dog":
                print()
                print("That's a bad idea.")

        # Using bone
        elif command_words[0].lower() == "give":
            if command_words[1].lower() == "bone":
                print()
                print("The dog gladly took the bone, wagging his tail."
                      "\nHe seems very happy now.")
                room_list[3].description = "You are in a garden of dead and rotted plants. There is a docile dog biting on a bone. " \
                                           "\nThere is a door to the south."
                item_list[5].room = 3

        # Check Inventory
        elif action.lower() == "inventory" or action.lower() == "check inventory":
            print()
            print("Inventory:")
            for item in item_list:
                if item.room == -1:
                    print(item.name)

        # Pick up items
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

        # Drop items
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

        # Quit action
        elif action.lower() == "q" or action.lower() == "quit":
            print()
            print("Goodbye.")
            done = True

        # Unknown input
        else:
            print()
            print("That is an invalid command.")

        # End of game
        if current_room == 10:
            done = True


main()
