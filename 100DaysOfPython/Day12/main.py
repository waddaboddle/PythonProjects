# # Scope
#
# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function {enemies}")  # Will output the enemies called within the function
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")
#
#
# # Local Scope
#
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()

# Global Scope

# player_health = 10  # Global variables
#
#
# def game():
#     def drink_potion():  # Local scope
#         potion_strength = 2  # Local variables
#         print(player_health)


# drink_potion() cant call when within another function

# No block scope in python

# game_level = 3
# enemies = ["skeleton", "zombies", "aliens"]
#
# def create_enemy():
#     if game_level < 5:
#         new_enemy = enemies[0]
#
#     print(new_enemy) #If outside this funtion cant be accessed

# things in functions are local scoped
# things in if and for loops are global

# enemies = 1
#
#
# def increase_enemies():
#     # global enemies # takes the global enemies and tries to modify it. often not desirable
#     # enemies = 2 # Don't give local and global variables the same name
#     print(f"enemies inside function {enemies}")
#     return enemies + 1
#
#
# enemies = increase_enemies() # Like this you can modify global variables by calling a function
# print(f"enemies outside function: {enemies}")

# Global Constants

PI = 3.14159 # all upper case means it is not to be changed
URL = "https://www.google.com"


