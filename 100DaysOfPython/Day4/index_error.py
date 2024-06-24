# states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]
#
# # print(states_of_america[4]) #index out of range
#
# num_of_states = len(states_of_america)
#
# print(states_of_america[num_of_states - 1])
#
# # dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",
# #                "Tomatoes", "Celery", "'Potatoes'"]
#
# fruits = ["a", "b", "c"]
# vegetables = ["d", "e", "f"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"] #0
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"] #1

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1]) # dirty_dozen[index number of the list amongst the lists][index number within the selected list]
