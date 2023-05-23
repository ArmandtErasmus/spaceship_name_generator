# import random module to project
from random import randint

# list of random names
list_names = ["Falcon", "Starship", "Deathstar", "Void", "Star Rider", "Nebula Surfer"]
list_adjectives = ["Fluffy", "Angry", "Silly", "Majestic", "Brave"]
list_colours = ["Silver", "Red", "Blue", "Green", "Yellow", "Pink"]

# introduction to the program
print("Welcome to the Spaceship Name Generator!")

# get and store the name of the user
user_name = "Commander " + input("What is your first name?\n")

# greet the user
print(f"Welcome to the Intergalactical Spaceship Engineering Centre {user_name}!")

# get user location
location = str(input("Are you registering your spaceship from the 'USA' or the 'UK'?\n"))

# check for incorrect input
if location not in set(['USA', 'UK']):
  # get correct input
  location = input("Incorrect input. Please enter 'USA' or 'UK'.\n")
  
# location id list and empty place holder 
location_id_list = ["USS", "HMS"]
location_id = ""

# determine user id
if location == "USA":
  location_id = location_id_list[0]
else:
  location_id = location_id_list[1]

# get user animal name
favourite_animal = str(input("What is your favourite animal?\n"))

# get user cool name
cool_word = str(input("Enter a word that you think sounds cool.\n"))

# generate spaceship name
spaceship_name = location_id + " " + list_colours[randint(0, 5)] + " " + list_adjectives[randint(0, 4)] + " " + favourite_animal + " " + cool_word + " " + list_names[randint(0, 5)]

# print spaceship name
print(f"Your spaceship is ready {user_name}!\nThe name of your spaceship is: {spaceship_name}")
