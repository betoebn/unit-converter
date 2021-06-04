from tkinter import *
import pandas as pd
from area import Area

data = pd.read_csv("Book1.csv")


def ok():
    origin_unit = variable.get()
    destiny_unit = variable2.get()
    origin_qty = float(entry.get())
    decimal = int(decimals.get())
    area = Area(origin_unit=origin_unit, destiny_unit=destiny_unit, origin_qty=origin_qty, decimal=decimal)
    label5 = Label(text=f"Result: {area.convertor()}")
    label5.place(x=165, y=35)


# Creating a new window and configurations
window = Tk()
window.title("Convertor V0.1")
window.minsize(width=300, height=175)
window.maxsize(width=300, height=175)


# Dropdown Menus
# Units from dropdown menu
unit_from = data["Unit"].tolist()
variable = StringVar(window)
variable.set(unit_from[0])  # default value

w = OptionMenu(window, variable, *unit_from)
w.place(x=10, y=60)

button = Button(window, text="OK", command=ok)
button.place(x=138, y=95)

# Units to dropdown menu
unit_to = data["Unit"].tolist()
variable2 = StringVar(window)
variable2.set(unit_to[0])  # default value
w = OptionMenu(window, variable2, *unit_to)
w.place(x=160, y=60)


# Labels
label1 = Label(text="From:")
label1.place(x=60, y=13)
label2 = Label(text="To:")
label2.place(x=225, y=13)
label3 = Label(text="Decimals")
label3.place(x=125, y=125)


# Entries
entry = Entry(width=20)
# Add some text to begin with
entry.insert(END, string="Enter the origin value")
entry.place(x=13, y=35)


# Decimals
decimals = Entry(width=10)
# Add some text to begin with
decimals.insert(END, string="Decimals")
decimals.place(x=118, y=145)


window.mainloop()
