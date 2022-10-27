import random
destinations = ["Hawaii", "Alaska", "Wisonsin", "Florida"]

restaurants = ["McDonalds", "Arby's", "Wendy's", "Taco Bell"]

transportation = ["Plane", "Train", "Automobile", "Bike"]

entertainment = ["Backpacking", "Swimming", "Theater", "Gaming"]

def generate_trip():
    user_input = ''
    while user_input != "y":
        destination_selected_and_approved = get_user_satisfied_selection(destinations, "destination")
        transportation_selected_and_approved = get_user_satisfied_selection(transportation, "transportation")
        restaurant_selected_and_approved = get_user_satisfied_selection(restaurants, "restaurant")
        entertainment_selected_and_approved = get_user_satisfied_selection(entertainment, "entertainment")

        print("We have selected the destination of: " + destination_selected_and_approved)
        print("We have selected the restaurant of: " + restaurant_selected_and_approved)
        print("We have selected the transportation of: " + transportation_selected_and_approved)
        print("We have selected the entertainment of: " + entertainment_selected_and_approved)
        user_input = input("Do you like this trip? Enter y for yes")

    print(f'''Your finalized trip:
    You are going to {destination_selected_and_approved}
    you will be eating at {restaurant_selected_and_approved}
    you will be traveling by {transportation_selected_and_approved}
    and once you get there please enjoy {entertainment_selected_and_approved}''')
    print("Enjoy your trip!")

def get_user_satisfied_selection(list_of_options, type_of_selection):
    user_is_happy = False

    while user_is_happy == False:
        random_selected = get_random_selection(list_of_options)
        user_input_satisfied = input(f"We have selected {random_selected} as your {type_of_selection}. Enter y if you are satisfied with that choice\n")
        if user_input_satisfied == "y":
            user_is_happy = True
    return random_selected

def get_random_selection(list_of_options):
    return random.choice(list_of_options)
    

generate_trip()