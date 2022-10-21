

# (5 points): As a developer, I want to make at least three 
# commits with descriptive messages 
# (5 points):  As a developer, I want to store my destinations, 
# restaurants, mode of transportation, and entertainment in their 
# own separate Lists. 
# (5 points): As a user, I want a destination to be randomly 
# selected for my day trip. 
# (5 points): As a user, I want a restaurant to be randomly 
# selected for my day trip
# (5 points): As a user, I want a mode of transportation to be 
# randomly selected for my day trip. 
# (5 points): As a user, I want a form of entertainment to be 
# randomly selected for my day trip.
# (15 points): As a user, I want to be able to randomly re-select 
# a destination, restaurant, mode of transportation, and/or form 
# of entertainment if I don’t like one or more of those things.
# (10 points): As a user, I want to be able to confirm that my 
# day trip is “complete” once I like all of the random selections.
# (10  points): As a user, I want to display my completed trip in 
# the console
# (5 points): Single Responsibility: As a developer, I want all of
#  my functions to have a Single Responsibility. Remember, each 
# function should do just one thing!

from random import random


destinations = ["Chicago", "Minneapolis", "Portland", "Savannah"]
restaurants = ["Taco Bell", "Burger King", "Subway", "Starbucks"]
mode_of_transportation = ["Car", "Train", "Plane", "Helicopter"]
entertainment = ["Boat Tour", "Jazz Club", "Basketball Game", "Shopping"]

import random


def select_location():
   location = random.choice(destinations)
   print(f"Destination: {location}")


def select_restaurant():
    food = random.choice(restaurants)
    print(f"Restaurant: {food}")


def select_mode_of_transportation():
    vehicle = random.choice(mode_of_transportation)
    print(f"Transportation: {vehicle}")

def select_entertainment():
    fun = random.choice(entertainment)
    print(f"Entertainment: {fun} ")

def store_first_randomized():
    print("hmm")

def randomize_my_options():
    select_location()
    select_restaurant()
    select_mode_of_transportation()
    select_entertainment()

def satisfy_client():
    satisfied = False 
    while satisfied is False:
        answer = input("Do these options sound good to you? Y/N ") 
        if answer == "Y":
            satisfied = True
            print("That was easy! Enjoy your trip!")
            break  
        if answer == "N":
            choose_a_different_option()
            satisfied = True
        else:
            print("I'm not sure what you mean by that!")
            

def choose_a_different_option():
    print("working on this later")


def lets_go_on_a_trip():
    randomize_my_options()
    satisfy_client()


lets_go_on_a_trip()



# re_select = input('''Which aspect are you not satisfied with? 
# Destination/Restaurant/Transportation/Entertainment? ''')
#             if re_select == "Destination":
#                 print("Here's the only other place available")
#                 select_location()




