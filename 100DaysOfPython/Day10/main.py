# Functions with Outputs

# def format_names(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#
#     return f"{formatted_f_name} {formatted_l_name}"  # This output replaces the part of the function where it was called
#     # also computer stops reading the function here
#
#
# formated_string = format_names("muhaimin", "AHMED")
#
# print(formated_string)
# print(format_names("muhaimin", "AHMED"))

# Functions with multiple returns

# def format_names(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You did not provide valid inputs."
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#
#     return f"{formatted_f_name} {formatted_l_name}"  # This output replaces the part of the function where it was called
#     # also computer stops reading the function here
#
#
# print(format_names(input("First Name? "), input("Last Name? ")))

# Docstrings

def format_names(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"  # This output replaces the part of the function where it was called
    # also computer stops reading the function here


print(format_names(input("First Name? "), input("Last Name? ")))



