"""
   TASK-1: Create a program that converts temperatures between Celsius, Fahrenheit, and Kelvin scales
"""
from tkinter import *

# Convert function
def convert_temp():
    try:
        val = float(entry.get())
        unit = selected_unit.get()

        if unit == "Celsius":
            f = (val * 9/5) + 32
            k = val + 273.15
            result_label.config(text=f"Fahrenheit: {f:.2f}\nKelvin: {k:.2f}")

        elif unit == "Fahrenheit":
            c = (val - 32) * 5/9
            k = c + 273.15
            result_label.config(text=f"Celsius: {c:.2f}\nKelvin: {k:.2f}")

        elif unit == "Kelvin":
            c = val - 273.15
            f = (c * 9/5) + 32
            result_label.config(text=f"Celsius: {c:.2f}\nFahrenheit: {f:.2f}")
            
    except ValueError:
        result_label.config(text="Please enter a valid number!")


# Main window
root = Tk()
root.title("Temperature Converter")
root.geometry("350x250")
root.config(bg="#f2f2f2")

# Title
Label(root, text="Temperature Converter", font=("Arial", 14, "bold"), bg="#f2f2f2").pack(pady=10)

# Entry field
Label(root, text="Enter Value:", font=("Arial", 12), bg="#f2f2f2").pack()
entry = Entry(root, font=("Arial", 12), justify="center")
entry.pack(pady=5)

# Dropdown menu
selected_unit = StringVar()
selected_unit.set("Celsius")

Label(root, text="Select Unit:", font=("Arial", 12), bg="#f2f2f2").pack()
drop = OptionMenu(root, selected_unit, "Celsius", "Fahrenheit", "Kelvin")
drop.config(font=("Arial", 11))
drop.pack(pady=5)

# Convert button
Button(root, text="Convert", font=("Arial", 12, "bold"), command=convert_temp, bg="#4CAF50", fg="white").pack(pady=10)

# Result label
result_label = Label(root, text="", font=("Arial", 12), bg="#f2f2f2")
result_label.pack()

root.mainloop()
