# Using for loops with lists

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits) # this is after the loop

# loops with range

# for number in range(1, 11, 3):
#     print(number)

total = 0

for number in range(1, 101):
    total += number
print(total)
