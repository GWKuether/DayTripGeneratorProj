

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
from unittest import skip


destinations = ["Chicago", "Minneapolis", "Portland", "Savannah"]
restaurants = ["Taco Bell", "Burger King", "Subway", "Starbucks"]
mode_of_transportation = ["Car", "Train", "Plane", "Helicopter"]
entertainment = ["Boat Tour", "Jazz Club", "Basketball Game", "Shopping"]

import random

trip_1 = []

def greeting():
    print("Hello, here is a quick trip we put together for you!")


def select_location():
   location = random.choice(destinations)
   trip_1.append(location)
   print(f"Destination: {location}")


def select_restaurant():
    food = random.choice(restaurants)
    trip_1.append(food)
    print(f"Restaurant: {food}")


def select_mode_of_transportation():
    vehicle = random.choice(mode_of_transportation)
    trip_1.append(vehicle)
    print(f"Transportation: {vehicle}")

def select_entertainment():
    fun = random.choice(entertainment)
    trip_1.append(fun)
    print(f"Entertainment: {fun} ")

def randomize_my_options():
    greeting()
    select_location()
    select_restaurant()
    select_mode_of_transportation()
    select_entertainment()

def repeat_trip_back():
    print("Destination: " + trip_1[0])
    print("Restaurant: " + trip_1[1])
    print("Transportation: " + trip_1[2])
    print("Entertainment: " + trip_1[3])

def satisfy_client():
    satisfied = False 
    while satisfied is False:
        answer = input("Do these options sound good? Y/N ") 
        if answer == "Y":
            satisfied = True
            print("That was easy! Here's your final trip!")
            repeat_trip_back()
            break  
        if answer == "N":
            choose_a_different_option()
            satisfied = True
        else:
            print("I'm not sure what you mean by that!")
            

def choose_a_different_option():
    re_select = input('''Which aspect are you not satisfied with? 
Destination/Restaurant/Transportation/Entertainment? ''')
    if re_select == "Destination":
        print("Perhaps you'd like to travel somewhere else?")
        is_dupe = True
        while is_dupe is True:
            location = random.choice(destinations)
            if location == trip_1[0]:
                is_dupe = True
            else:
                location_2 = input("how about " + location + "? Y/N ")
                if location_2 == "Y":
                    print("Perfect, here's your final trip!")
                    trip_1[0] = location
                    repeat_trip_back()




def lets_go_on_a_trip():
    randomize_my_options()
    satisfy_client()


lets_go_on_a_trip()








