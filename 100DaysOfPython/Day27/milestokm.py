from tkinter import *


def convert():
    km_value = float(miles_input.get()) * 1.609
    km_label.config(text=km_value)


window = Tk()

window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Entry

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Label

miles_label = Label(text="Miles", font=("Arial", 12, "normal"))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Arial", 12, "normal"))
equal_label.grid(column=0, row=1)

km_label = Label(text=0, font=("Arial", 12, "bold"))
km_label.grid(column=1, row=1)

kilometer_label = Label(text="Km", font=("Arial", 12, "normal"))
kilometer_label.grid(column=2, row=1)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
