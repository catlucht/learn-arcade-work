import random


def main():
    """ Cat and Mouse Game """

    # Introduction
    print("Welcome to Cat and Mouse!")
    print("You are a mouse. You are running across the house")
    print("with the cat's favorite catnip.")
    print("The cat wants it back and is chasing you down!")
    print("Survive your journey to safety and outrun the cat.")
    print()

    done = False

    # Player stats
    mouse_feet_traveled = 0
    hunger = 0
    mouse_tiredness = 0
    cat_feet_traveled = -20
    cheese = 3

    # Player input options
    while not done:
        print("A. Eat a piece of cheese.")
        print("B. Run ahead at moderate speed.")
        print("C. Run ahead at full speed!")
        print("D. Hide and rest.")
        print("E. Status check.")
        print("F. Quit.")

        action = input("What is your choice? ")

        # --- Player inputs ---

        # Quit input
        if action.upper() == "F":
            print()
            print("Quitter!")

            done = True

        # Status check input
        elif action.upper() == "E":
            print()
            print("Feet traveled:", mouse_feet_traveled)
            print("Cheese left:", cheese)
            print("The cat is", mouse_feet_traveled - cat_feet_traveled, "feet behind you!")
            print()

        # Rest input
        elif action.upper() == "D":
            print()

            mouse_tiredness = 0
            print("You are rested!")

            my_number = random.randrange(1, 6)
            cat_feet_traveled += my_number

            print()

        # Full speed input
        elif action.upper() == "C":
            print()

            hunger += 1

            my_number = random.randrange(10, 17)
            mouse_feet_traveled += my_number
            print("You ran", my_number, "feet.")

            my_number = random.randrange(1, 4)
            mouse_tiredness += my_number

            my_number = random.randrange(7, 14)
            cat_feet_traveled += my_number

            print()

            # Random chance "oasis"
            for i in range(1):
                if random.randrange(15) == 0:
                    print("You found a hidey hole full of cheese!")
                    hunger = 0
                    mouse_tiredness = 0
                    cheese = 3
                    print()

        # Moderate speed input
        elif action.upper() == "B":
            print()

            hunger += 1
            mouse_tiredness += 1

            my_number = random.randrange(4, 9)
            print("You ran", my_number, "feet.")

            my_number = random.randrange(7, 14)
            cat_feet_traveled += my_number

            print()

            # Random chance "oasis"
            for i in range(1):
                if random.randrange(15) == 0:
                    print("You found a hidey hole full of cheese!")

                    hunger = 0
                    mouse_tiredness = 0
                    cheese = 3

                    print()

        # Cheese input
        elif action.upper() == "A":
            print()

            if cheese >= 1:
                print("You nibbled on some cheese.")
                hunger = 0
            else:
                print("You are out of cheese!")

            print()

        # --- Player feedback and end of game ---

        if not done and mouse_tiredness > 8:
            print("You died of immense fatigue!")
            done = True

        elif not done and mouse_tiredness > 5:
            print("You are getting tired.")
            print()

        if not done and cat_feet_traveled >= mouse_feet_traveled:
            print("The cat has caught you!")
            done = True

        elif not done and cat_feet_traveled >= mouse_feet_traveled - 15:
            print("The cat is getting close!")
            print()

        if not done and hunger >= 6:
            print("You died of hunger...")
            done = True

        elif not done and hunger >= 4:
            print("You are hungry! Eat some cheese or parish!")
            print()

        if not done and mouse_feet_traveled >= 200:
            print("You made it to safety! You win!")
            done = True

main()
