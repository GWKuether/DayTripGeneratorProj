import random

destination_1 = {
    "location": "Savannah",
    "restaurant": ["Subway", "Starbucks", "Taco Bell", "Burger King"],
    "entertainment": ["Boat Tour", "Jazz Club", "Basketball Game", "Shopping"],
    "transportation": ["Car", "Train", "Plane", "Helicopter"]
}

destination_2 = {
    "location": "Chicago",
    "restaurant": ["Subway", "Starbucks", "Taco Bell", "Burger King"],
    "entertainment": ["Boat Tour", "Jazz Club", "Basketball Game", "Shopping"],
    "transportation": ["Car", "Train", "Plane", "Helicopter"]
}

destination_3 = {
    "location": "Minneapolis",
    "restaurant": ["Subway", "Starbucks", "Taco Bell", "Burger King"],
    "entertainment": ["Boat Tour", "Jazz Club", "Basketball Game", "Shopping"],
    "transportation": ["Car", "Train", "Plane", "Helicopter"]
}

destination_4 = {
    "location": "Portland",
    "restaurant": ["Subway", "Starbucks", "Taco Bell", "Burger King"],
    "entertainment": ["Boat Tour", "Jazz Club", "Basketball Game", "Shopping"],
    "transportation": ["Car", "Train", "Plane", "Helicopter"]
}



def generate_trip(location, restaurant, entertainment, transportation):
    place = location
    food = restaurant
    fun = entertainment
    vehicle = transportation
    food_1 = random.choice(food)
    fun_1 = random.choice(fun)
    vehicle_1 = random.choice(vehicle)

    print("how about we go to " + place + "?")
    print("We can eat at " + food_1)
    print("After dinner we can enjoy " + fun_1)
    print("And of course we would travel around via " + vehicle_1 + "!")
    

generate_trip(**destination_1)
generate_trip(**destination_2)
generate_trip(**destination_3)
generate_trip(**destination_4)





def get_user_satisfied_selection():
    user_is_happy = False
    while user_is_happy == False:
        answer = input("If you are satisfied with this trip type 'y'")
        if answer == "y":
            print("Awesome, here's your final trip")



    

# generate_trip()






