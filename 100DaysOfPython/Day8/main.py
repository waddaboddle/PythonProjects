# Review
# Create a funtion called greet().
# Write 3 print statements inside the function
# Call the greet() function and run your code

# def greet(name):
#     print("Hi " + name)
#     print("How are you " + name)
#     print("Bye " + name)
#
#
# greet("Muhaimin") # In this case name is the parameter, "Muhaimin" is the argument.

# Functions with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How is it like in {location}")


# greet_with("Muhaimin", "Montreal")

# greet_with("Nowhere ", "Muhaimin ") positional argument if nothing is specified in terms of order of the parameters

# Key word arguments

greet_with(location="Montreal ", name="Muhaimin ")
