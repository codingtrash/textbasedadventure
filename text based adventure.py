#Author: Daniel Binns
#Date: 4/4/2021
#App name - Text-based adventure

print("Welcome to TEXT-BASED ADVENTURE (Version 1.0)")
print("Here are the rules:")
print("For every problem you encounter on your journey, there will be two options to choose from.")
print("Choose wisely, at any time the wrong move can lead to death.")
print("What will you name your character?")
charName = input()
print("Welcome, " + charName + ".")
print("Press 'y' to start your adventure.")
while (True):
    ready = input().lower()
    if ready == "y":
        break
    else:
        print("I'm asking nicely, please press 'y' to continue.")
print("You wake up after 15 years asleep...")
print("You start to walk in the direction of a building")
print("You find a key, what do you do?")
print("OPTIONS: put it back or stash for later")
while (True):
    option1 = input().lower()
    if option1 == "put it back":
        break
    elif option1 == "stash for later":
        break
    else:
        print("Invalid input, please retype your answer.")
print("YOU HAVE SELECTED: " + option1)
print("As you continue to get closer, you see a monster in the way")
print("What do you do?")
print("OPTIONS: Avoid or Battle")
while (True):
    option2 = input().lower()
    if option2 == "avoid":
        break
    elif option2 == "battle":
        print("You have died.")
        print("Your choices were " + option1 + ", " + option2)
        quit("Game over")
    else:
        print("Invalid input, please retype your answer.")
print("As you approach the building, you see it is a castle.")
print("Is this your home?")
print("You get closer and closer")
print("OPTIONS: Rest or Keep walking")
while (True):
    option3 = input().lower()
    if option3 == "rest":
        break
    elif option3 == "keep walking":
        print("You pass out after walking so much, vultures kill you in your deep sleep")
        print("Your choices were " + option1 + ", " + option2 + ", " + option3)
        quit("Game over")
    else:
        print("Invalid input. Please retype your answer")
print("YOU HAVE SELECTED: " + option3)
print("Finally, you make it to the door")
print("Did you keep the key?")
print("OPTIONS: Yes or No")
while (True):
    option4 = input().lower()
    if option4 == "yes":
        break
    elif option4 == "no":
        print("You need the key to continue.")
        print("Your choices were: " + option1 + ", " + option2 + ", " + option3 + ", " + option4 + ".")
        quit("Game over")
    else:
        print("Invalid input. Please retype your answer.")
print("You have successfully finished TEXT BASED ADVENTURE")
print("Your choices were: " + option1 + ", " + option2 + ", " + option3 + ", " + option4 + ".")
