# Welcome to the game. Want to play?
print("Welcome to the Adventure Game!")
print("Your journey begins here...")
""""
Author: Kyle Kuhn
Version 1.0
Description: This program is for your adventure.
""""
# Asks for name
player_name = input("What is your name adventurer?")

# Concatenate string into single print
print(f"Welcome, {player_name}! Your journey begins now.")

# Describe this starting area
starting_area = """
You find yourself in a moonlit forest.
The sound of wind and leaves fills the area.
A faint path leads deeper into the unknown....
"""
print(starting_area)

# Ask player for their decision
decision = input("Do you want to take the path? (yes or no): ").lower()

# Response based on player's decision

if decision == "yes":
    print(f"Brave choice, {player_name}, you are going to take the path deeper into the forest.")
elif decision == "no":
    print(player_name + ", you decide to wait. Maybe you will be stronger later")
else:
    print("Confusion. Do you want to take the path or stay still?")