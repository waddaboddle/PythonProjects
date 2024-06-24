# with open("file1.txt") as file1:
#     data1 = file1.readlines()
#
# with open("file2.txt") as file2:
#     data2 = file2.readlines()
#
#
# result = [int(num) for num in data1 if num in data2]
#
# # Write your code above 👆
#
# print(result)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}
print(student_dict)
# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)

# loop through rows of the data frame

for (index, row) in student_data_frame.iterrows():
    print(row.score)
