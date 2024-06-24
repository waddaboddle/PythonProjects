from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:

        try:

            with open("data.json", mode="r") as data_file:
                # Read the old data
                data = json.load(data_file)

        except (FileNotFoundError, json.decoder.JSONDecodeError):

            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:

            # Updating old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:

            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #

def search_info():
    website = website_input.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website,
                                message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message="No Details for the Website Exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

# Labels --------------------------------------------------

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Buttons -------------------------------------------------

add_button = Button(text="Add", width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)

generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(column=2, row=3)

search_button = Button(text="Search", width=15, command=search_info)
search_button.grid(column=2, row=1)

# Entries --------------------------------------------------

website_input = Entry(width=33)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=53)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "muhai0503@gmail.com")

password_input = Entry(width=33)
password_input.grid(column=1, row=3)

window.mainloop()
