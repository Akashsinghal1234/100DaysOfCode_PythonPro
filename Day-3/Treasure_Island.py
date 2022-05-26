print("Welcome to Treasure Island.")
print("Your mission is to find the Treasure.")
path = input("You're at the cross road. Where do you want to go? Type 'left' or 'right' ")
if path == "right":
    print("Oops, you got stuck in a ketchup pool, game over.")
else:
    pool = input("You have encountered an chocolate house ! Do you want to eat a chocolate frog or chocolate pencil ? Type 'frog' or 'pencil' ")
    if pool == "frog":
        print("Oops, the frog was real, game over .")
    else:
        gate = input("Your stomach is now full, Do you want to enter red, blue or yellow gate ? Type 'red', 'blue', 'yellow' ")
        if gate == "red":
            print("Game over.")
        elif gate == "blue":
            print("Game over.")
        else:
            print("Yayy, We found the Treasure ! Oops wait it was in a game ;) ")