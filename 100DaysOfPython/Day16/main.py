from turtle import Turtle, Screen

# Object-Oriented Programming (OOP)
# attributes: variable associated with an object
# methods: functions of the object
# Class is the type of the object

# car = BluePrint() classes are Pascal cased
# this activates the construction of the object from this blueprint
#
# timmy = Turtle() # Create a new object
# print(timmy)
# timmy.shape("turtle") # Methods
# timmy.color("DarkSeaGreen")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight) # Attributes
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon", ["Pikachu", "Charizard", "Greninja"])
table.add_column("Type", ["Electric", "Fire", "Water"])
table.align = "l"
print(table)
