

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
dest_storage = []


def greeting():
    name = input("What is your name? ")
    print(F"Hello {name}, here is a quick trip we put together for you!")


def select_location():
   location = random.choice(destinations)
   trip_1.append(location)
   dest_storage.append(location)
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
        answer = answer.upper()
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
# put in a loop here
    if re_select == "Destination":
        exhaust_destinations()
    elif re_select == "Restaurant":
        exhaust_restaurants()
    elif re_select == "Transportation":
        exhaust_transportation()
    elif re_select == "Entertainment":
        exhaust_entertainment()
    else:
        print("I'm not sure what you mean by that! Let's try again.")

def re_start_ex_dest():
    exhaust_destinations()

def exhaust_destinations():
    print("Perhaps you'd like to travel somewhere else?")
    is_dupe = True
    while is_dupe is True:
        location = random.choice(destinations)
        if location == trip_1[0]:
            is_dupe = True
        else:
            answer_2 = input("how about " + location + "? Y/N ")
            answer_2 = answer_2.upper()
            dest_storage.append(location)
            if answer_2 == "Y":
                print("Perfect, here's your final trip!")
                trip_1[0] = location
                is_dupe = False
                repeat_trip_back()
                break
            elif answer_2 == "N":
                is_dupe_2 = True
                while is_dupe_2 is True:
                    location_2 = random.choice(destinations)
                    if location_2 == dest_storage[0]:
                        is_dupe_2 = True
                    elif location_2 == dest_storage[1]:
                        is_dupe_2 = True
                    else:
                        answer_3 = input("how about " + location_2 + "? Y/N ")
                        answer_3 = answer_3.upper()
                        dest_storage.append(location_2)
                        if answer_3 == "Y":
                            print("Perfect, here's your final trip!")
                            trip_1[0] = location_2
                            is_dupe = False
                            is_dupe_2 = False
                            repeat_trip_back()
                            break
                        elif answer_3 == "N":
                            is_dupe_3 = True
                            while is_dupe_3 is True:
                                location_3 = random.choice(destinations)
                                if location_3 == dest_storage[0]:
                                    is_dupe_3 = True
                                elif location_3 == dest_storage[1]:
                                    is_dupe_3 = True
                                elif location_3 == dest_storage[2]:
                                    is_dupe_3 = True
                                else:
                                    answer_4 = input("how about " + location_3 + "? Y/N ")
                                    answer_4 = answer_4.upper()
                                    dest_storage.append(location_3)
                                    if answer_4 == "Y":
                                        print("Perfect, here's your final trip!")
                                        trip_1[0] = location_3
                                        is_dupe = False
                                        is_dupe_2 = False
                                        is_dupe_3 = False
                                        repeat_trip_back()
                                        break
                                    elif answer_4 == "N":
                                        choose_your_destination = input("I'm sorry, those are all of the locations we had on sale. If you would like to go somewhere else, please type it in: ")
                                        trip_1[0] = choose_your_destination
                                        print("Okay, here's the final trip!")
                                        is_dupe = False
                                        is_dupe_2 = False
                                        is_dupe_3 = False
                                        repeat_trip_back()
                                        break
                                    else:
                                        print("I'm not sure what you mean by that, please try again.")
                                        dest_storage.pop(3)
                                        dest_storage.pop(2)
                                        dest_storage.pop(1)
                                        re_start_ex_dest()
                                        is_dupe = False
                                        break     
                        else:
                            print("I'm not sure what you mean by that, please try again.")
                            dest_storage.pop(2)
                            dest_storage.pop(1)
                            re_start_ex_dest()
                            is_dupe = False
                            break                       
            else:
                print("I'm not sure what you mean by that, please try again.")
                dest_storage.pop(1)
                re_start_ex_dest()
                is_dupe = False
                break     

# add loop backs if user input is not correct

def lets_go_on_a_trip():
    randomize_my_options()
    satisfy_client()


lets_go_on_a_trip()








