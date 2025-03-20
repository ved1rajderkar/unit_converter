import tkinter as tk
from tkinter import ttk

# Conversion function
def convert():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        # Temperature conversion
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = (value * 9/5) + 32
            elif to_unit == "Kelvin":
                result = value + 273.15
            else:
                result = value

        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (value - 32) * 5/9
            elif to_unit == "Kelvin":
                result = (value - 32) * 5/9 + 273.15
            else:
                result = value

        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = value - 273.15
            elif to_unit == "Fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            else:
                result = value

        # Length conversion
        length_units = {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084}
        if from_unit in length_units and to_unit in length_units:
            result = value * length_units[to_unit] / length_units[from_unit]

        # Weight conversion
        weight_units = {"Grams": 1, "Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274}
        if from_unit in weight_units and to_unit in weight_units:
            result = value * weight_units[to_unit] / weight_units[from_unit]

        # Display result
        label_result.config(text=f"Result: {round(result, 4)} {to_unit}")

    except ValueError:
        label_result.config(text="Invalid input!")

# UI Setup
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#f4f4f4")

# Title Label
title_label = tk.Label(root, text="Unit Converter", font=("Arial", 16, "bold"), bg="#f4f4f4")
title_label.pack(pady=10)

# Input Field
entry_value = tk.Entry(root, font=("Arial", 14), justify="center")
entry_value.pack(pady=5)

# Dropdowns
units = {
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Length": ["Meters", "Kilometers", "Miles", "Feet"],
    "Weight": ["Grams", "Kilograms", "Pounds", "Ounces"]
}
all_units = sum(units.values(), [])  # Flatten unit list

combo_from = ttk.Combobox(root, values=all_units, font=("Arial", 12))
combo_from.set("Celsius")
combo_from.pack(pady=5)

combo_to = ttk.Combobox(root, values=all_units, font=("Arial", 12))
combo_to.set("Fahrenheit")
combo_to.pack(pady=5)

# Convert Button
convert_button = tk.Button(root, text="Convert", font=("Arial", 14), command=convert, bg="#4CAF50", fg="white")
convert_button.pack(pady=10)

# Result Label
label_result = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"), bg="#f4f4f4")
label_result.pack(pady=10)

# Run App
root.mainloop()
