import tkinter as tk
from tkinter import messagebox, font
import joblib

# Load the trained model
model = joblib.load('waterquality.pkl')

# Function to perform prediction
def predict():
    try:
        # Get input values from the entry fields
        do = float(do_entry.get())
        ph = float(ph_entry.get())
        co = float(co_entry.get())
        bod = float(bod_entry.get())
        na = float(na_entry.get())
        tc = float(tc_entry.get())
        year = int(year_entry.get())

        # Perform the prediction using the loaded model
        prediction = model.predict([[do, ph, co, bod, na, tc, year]])

        # Show the prediction in a message box
        messagebox.showinfo("Prediction", f"The predicted result is {prediction}")

    except ValueError:
        # Show error message if input values are not valid
        messagebox.showerror("Error", "Please enter valid numeric values")

# Create Tkinter window
window = tk.Tk()
window.title("Water Quality Prediction")
window.geometry("400x300")  # Set the size of the window (width x height)

# Define font
font_label = font.Font(size=12)
font_entry = font.Font(size=12)

# Create entry fields for input features
do_label = tk.Label(window, text="DO:", font=font_label)
do_label.grid(row=0, column=0)
do_entry = tk.Entry(window, font=font_entry)
do_entry.grid(row=0, column=1)

ph_label = tk.Label(window, text="pH:", font=font_label)
ph_label.grid(row=1, column=0)
ph_entry = tk.Entry(window, font=font_entry)
ph_entry.grid(row=1, column=1)

co_label = tk.Label(window, text="CO:", font=font_label)
co_label.grid(row=2, column=0)
co_entry = tk.Entry(window, font=font_entry)
co_entry.grid(row=2, column=1)

bod_label = tk.Label(window, text="BOD:", font=font_label)
bod_label.grid(row=3, column=0)
bod_entry = tk.Entry(window, font=font_entry)
bod_entry.grid(row=3, column=1)

na_label = tk.Label(window, text="NA:", font=font_label)
na_label.grid(row=4, column=0)
na_entry = tk.Entry(window, font=font_entry)
na_entry.grid(row=4, column=1)

tc_label = tk.Label(window, text="TC:", font=font_label)
tc_label.grid(row=5, column=0)
tc_entry = tk.Entry(window, font=font_entry)
tc_entry.grid(row=5, column=1)

year_label = tk.Label(window, text="Year:", font=font_label)
year_label.grid(row=6, column=0)
year_entry = tk.Entry(window, font=font_entry)
year_entry.grid(row=6, column=1)

# Create predict button
predict_button = tk.Button(window, text="Predict", command=predict, font=font_label)
predict_button.grid(row=7, column=0, columnspan=2)

# Run Tkinter event loop
window.mainloop()
