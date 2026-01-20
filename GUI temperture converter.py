import tkinter as tk
from tkinter import ttk, messagebox

# Main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x300")
root.resizable(False, False)

# Variables
temperature = tk.StringVar()
from_unit = tk.StringVar(value="Celsius")
to_unit = tk.StringVar(value="Fahrenheit")

# Conversion function
def convert_temperature():
    try:
        temp = float(temperature.get())

        if from_unit.get() == "Celsius" and to_unit.get() == "Fahrenheit":
            result = (temp * 9/5) + 32

        elif from_unit.get() == "Fahrenheit" and to_unit.get() == "Celsius":
            result = (temp - 32) * 5/9

        elif from_unit.get() == "Celsius" and to_unit.get() == "Kelvin":
            result = temp + 273.15

        elif from_unit.get() == "Kelvin" and to_unit.get() == "Celsius":
            result = temp - 273.15

        elif from_unit.get() == "Fahrenheit" and to_unit.get() == "Kelvin":
            result = (temp - 32) * 5/9 + 273.15

        elif from_unit.get() == "Kelvin" and to_unit.get() == "Fahrenheit":
            result = (temp - 273.15) * 9/5 + 32

        else:
            result = temp  # same unit

        result_label.config(text=f"Result: {result:.2f}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

# Widgets
tk.Label(root, text="Temperature Converter", font=("Arial", 16, "bold")).pack(pady=10)

tk.Entry(root, textvariable=temperature, font=("Arial", 12)).pack(pady=5)

ttk.Combobox(root, textvariable=from_unit,
             values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly").pack(pady=5)

ttk.Combobox(root, textvariable=to_unit,
             values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly").pack(pady=5)

tk.Button(root, text="Convert", command=convert_temperature).pack(pady=15)

result_label = tk.Label(root, text="Result:", font=("Arial", 12))
result_label.pack()

root.mainloop()g
