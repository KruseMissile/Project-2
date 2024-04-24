"""
Author:         Owen Kruse
Date:           4/25/2024
Assignment:     Project 2
Course:         CPSC1050
Lab Section:    001

https://github.com/KruseMissile/Project-2.git
"""

import random

class Inventory:
    def __init__(self):
        self.items = []

    def pick_up(self, item):
        self.items.append(item)

    def get_item(self, item):
        if item in self.items:
            return item
        else:
            return None

    def use_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return True
        else:
            return False



class Health:
    def __init__(self):
        self.health = 100

    def lose_health(self, amount):
        self.health -= amount

    def gain_health(self, amount):
        self.health += amount

    def get_health(self):
        return self.health




class ExitNotFoundError(Exception):
    
    #This initializes this exception class
    def __init__(self, exit_choice, message="Option not found"):
        self.exit_choice = exit_choice
        self.message = message
        super().__init__(message)

#This is the actual message string of the exception
    def __str__(self):
        return f"{self.exit_choice} -> {self.message}"
    

class Place:
    #This is a function that initializes the variables in the class "Room"
    def __init__(self,name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits

#This is a function that returns the room name
    def get_name(self):
        return self.name

#This is the function that returns the description of the room
    def get_description(self):
        return self.description

#Function where you can get the exits of the current room
    def get_exits(self):
        return self.exits
#Function of a list of the exits with a new line in between
    def list_exits(self):
        return '\n'.join(self.exits)
#This is the actual string printed whenever a room is entered
    def __str__(self):
        return f"{self.name}: {self.description}\n\nMoves:\n{self.list_exits()}"

class AdventureMap:
    #Initialize the map
    def __init__(self):
        self.map = {}
    
    #Funciton where places can be added to the map
    def add_place(self, place):
        self.map[place.name.lower()] = place
    #Function where if they choose an exit it will go to the exit if not an exception error occurs
    def get_place(self, name):
        place = self.map.get(name.lower())
        if place:
            return place
        else:
            raise ExitNotFoundError(name)
    



if __name__ == "__main__":
    #All places are being added
    
    inventory = Inventory()
    health = Health()
    
    adventure_map = AdventureMap()
    adventure_map.add_place(Place("Woods", "Your in the middle of the woods by yourself and need to use skills to survive. Here you can gather supplies you might need in the future and store in your inventory.", ['Campsite', 'River', 'Cave']))
    adventure_map.add_place(Place("Campsite", "You are now in your campsite where you are safe from any danger with options of ways to gain health or exit", ['Woods', 'Cave']))
    adventure_map.add_place(Place("River", "You are alongside the river with many options that can heal or hurt you. Choose Right!", ["Woods"]))
    adventure_map.add_place(Place("Cave", "You are in a very cold cave and cannot see deep into it. Be wary there might be danger in here", ["Campsite", "Woods"]))
    

    #Starting statement and starting the game in the study room
    print("\nWelcome to Owen's Survival Game! Entering the Woods alone. To leave the game, please type exit to get picked up by a helicopter and be rescued.\n")
    print("Instructions:\nYou are gonna be given options depending on your location. You can type out the action you want to be done exactly how it is put in the options. Or, type the name of place you want to go and you will travel there. You will start out with 100 health and can lose health as well as gain health by doing correct options.")
    
    the_place = adventure_map.get_place("Woods")
    
    
    print(the_place)
    
  
    choice = 'play'

    while choice != 'exit':
        
        
        try:
            print()
            # Asks for an action if the user is in the Campsite
            if the_place.get_name() == "Campsite":
                while the_place.get_name() == "Campsite":
                    if health.get_health() <= 0:
                        print("Your health is 0 or less. You have died. Game over.")
                        exit()
                    print("Please choose an action: sleep, cook fish(1/4 chance it is cooked raw), drink water, or choose an exit:", the_place.get_exits())
                    action_choice = input().lower()
                    exit_choice = action_choice.title()
                    if exit_choice in the_place.get_exits():
                        # If action_choice is an exit option, update the current place
                        the_place = adventure_map.get_place(exit_choice)
                        print(the_place)
                        continue
                    # Perform actions based on user choice
                    elif action_choice == "sleep":
                        print("You decide to sleep and regain 20 health.")
                        health.gain_health(20)
                        current_health = health.get_health()
                        print("Current Health:", current_health)
                    elif action_choice == "cook fish":
                        if "wood" in inventory.items and "fish" in inventory.items:
                            if random.random() < 0.25:  # 25% chance the fish is raw
                                print("Oh no! The fish is raw! You die from food poisoning!")
                                exit()
                            
                            else:
                                print("You use some wood to start a fire and cook the fish. Delicious!")
                                inventory.use_item("wood")
                                inventory.use_item("fish")
                                health.gain_health(10)
                                current_health = health.get_health()
                                print("Current Health:", current_health)
                        else:
                            print("You need both wood and fish in your inventory to cook.")
                            health.lose_health(20)  # Lose 20 health for invalid action
                            current_health = health.get_health()
                            print("Current Health:", current_health)
                    elif action_choice == "drink water":
                        print("You drink some refreshing water from your canteen.")
                        health.gain_health(5)
                        current_health = health.get_health()
                        print("Current Health:", current_health)
                    
                    elif action_choice == "exit":
                        # Let the loop continue to handle exit logic
                        print("\nA helicopter has arrived to pick you up! Thank you for playing!")
                        exit()
                    else:
                        print("Invalid action. You lost health. Please choose again.")
                        health.lose_health(20)  # Lose 20 health for invalid action
                        current_health = health.get_health()
                        print("Current Health:", current_health)
            elif the_place.get_name() == "Woods":
                while the_place.get_name() == "Woods":

                    if health.get_health() <= 0:
                        print("Your health is 0 or less. You have died. Game over.")
                        exit()
                    print("Please choose an action: collect wood, collect worms, collect fishing rod, or choose an exit:", the_place.get_exits())
                    action_choice = input().lower().strip()
                    exit_choice = action_choice.title()
                    # Perform actions based on user choice
                    if exit_choice in the_place.get_exits():
                        # If action_choice is an exit option, update the current place
                        the_place = adventure_map.get_place(exit_choice)
                        print(the_place)
                        
                    elif action_choice == "collect wood":
                        print("You collect some wood and add it to your inventory.")
                        inventory.pick_up("wood")
                    elif action_choice == "collect worms":
                        print("You search the ground and find some worms.")
                        inventory.pick_up("worms")
                    elif action_choice == "collect fishing rod":
                        print("You find a fishing rod hidden behind a bush.")
                        inventory.pick_up("fishing rod")
                    
                    elif action_choice == "exit":
                        # Let the loop continue to handle exit logic
                        print("\nA helicopter has arrived to pick you up! Thank you for playing!")
                        exit()
                    else:
                        print("Invalid action. You lost health. Please choose again.")
                        health.lose_health(20)  # Lose 20 health for invalid action
                        current_health = health.get_health()
                        print("Current Health:", current_health)
            # Asks for an action if the user is in the River
            elif the_place.get_name() == "River":
                while the_place.get_name() == "River":

                    if health.get_health() <= 0:
                        print("Your health is 0 or less. You have died. Game over.")
                        exit()
                    print("Please choose an action: drink water, fish, bathe, or choose an exit:", the_place.get_exits())
                    action_choice = input().lower().strip()
                    exit_choice = action_choice.title()
                    # Perform actions based on user choice
                    if exit_choice in the_place.get_exits():
                        # If action_choice is an exit option, update the current place
                        the_place = adventure_map.get_place(exit_choice)
                        print(the_place)
                        
                    elif action_choice == "drink water":
                        print("You drink some fresh water from the river.")
                        health.gain_health(5)
                        current_health = health.get_health()
                        print("Current Health:", current_health)
                    elif action_choice == "fish":
                        if "fishing rod" in inventory.items and "worms" in inventory.items:
                            print("You cast your line into the river and wait patiently.")
                            print("After a while, you catch a fish!")
                            inventory.pick_up("fish")
                        else:
                            print("You need both a fishing rod and worms in your inventory to fish.")
                            health.lose_health(20)  # Lose 20 health if action can't be performed
                            current_health = health.get_health()
                            print("Current Health:", current_health)
                    elif action_choice == "bathe":
                        print("You take a refreshing dip in the cool river water.")
                        health.gain_health(5)
                        current_health = health.get_health()
                        print("Current Health:", current_health)
                    
                    elif action_choice == "exit":
                        # Let the loop continue to handle exit logic
                        print("\nA helicopter has arrived to pick you up! Thank you for playing!")
                        exit()
                    else:
                        print("Invalid action. You lost health. Please choose again.")
                        health.lose_health(20)  # Lose 20 health for invalid action
                        current_health = health.get_health()
                        print("Current Health:", current_health)
            # Asks for an action if the user is in the Deep Cave
            elif the_place.get_name() == "Cave":
                while the_place.get_name() == "Cave":

                    if health.get_health() <= 0:
                        print("Your health is 0 or less. You have died. Game over.")
                        exit()
                    print("Please choose an action: explore the cave, observe fish bones, or choose an exit:", the_place.get_exits())
                    action_choice = input().lower().strip()
                    exit_choice = action_choice.title()
                    # Perform actions based on user choice
                    if exit_choice in the_place.get_exits():
                        # If action_choice is an exit option, update the current place
                        the_place = adventure_map.get_place(exit_choice)
                        print(the_place)
                        continue
                    elif action_choice == "explore the cave":
                        print("You enter deeper into the cave and encounter a bear!")
                        print("The bear attacks you, and you don't survive.")
                        exit()
                    elif action_choice == "observe fishbones":
                        print("You observe a pile of fishbones and pick some meat off.")
                        print("You eat the meat, gaining 5 health.")
                        health.gain_health(5)
                        current_health = health.get_health()
                        print("Current Health:", current_health)
                    
                    elif action_choice == "exit":
                        # Let the loop continue to handle exit logic
                        print("\nA helicopter has arrived to pick you up! Thank you for playing!")
                        exit()
                    else:
                        print("Invalid action. You lost health. Please choose again.")
                        health.lose_health(20)  # Lose 20 health for invalid action
                        current_health = health.get_health()
                        print("Current Health:", current_health)
            else:
                # Asks for an exit if not in Campsite, Woods, River, or Deep Cave
                print("Please choose an exit: ")
                exit_choice = input().lower().strip()
                
                # Checks if the user wants to end the game
                if exit_choice == 'exit':
                    choice = 'exit'
                    break
                
                # If they choose a valid exit, update the current place
                if exit_choice in the_place.get_exits():
                    the_place = adventure_map.get_place(exit_choice)
                    print(the_place)
                else:
                    # If not a valid exit, raise an error
                    if exit_choice not in the_place.get_exits():
                        raise ExitNotFoundError(exit_choice)
                
        except ExitNotFoundError as e:
            print(e)