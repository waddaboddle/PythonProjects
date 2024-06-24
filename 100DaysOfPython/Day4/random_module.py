import random
import mymodule

random_integer = random.randint(1, 10)

print(random_integer)

# print(mymodule.pi)

random_float = random.random()
print(random_float)
print(5*random_float) # by multiplying we can vary the range

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")
