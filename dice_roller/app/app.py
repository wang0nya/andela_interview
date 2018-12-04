import random


def dice_roller():
    return(random.randint(1,6))


def roll_again():
    while True:
        roll = input("Play again? Press (y)es / (q)uit.\n")
        if roll == "y":
            print(dice_roller())
            continue
        elif roll == "q":
            break
        else:
            print("Please enter a valid input. 'y' to continue, 'q' to quit.")
    

if __name__ == "__main__":
    print(dice_roller())
    roll_again()
