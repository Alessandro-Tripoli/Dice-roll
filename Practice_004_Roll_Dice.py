#In this program we will simulate a game of rolling dice between two players.
#Each die is 1 through 6 and there are two die.
import random

def roll(sides = 6):
    value_rolled = random.randint(1, sides)
    return value_rolled

def main():
    sides = 6
    rolling = True
    while rolling:
        second_roll = input("Ready to roll? Enter roll. Q=Quit. ")
        if second_roll.lower() != "q":
            value_rolled = roll(sides)
        print("You rolled a ", value_rolled)
    else:
        rolling = False
        print("Thanks for playing")
main()
