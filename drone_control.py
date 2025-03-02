import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Drone Control Panel")
root.geometry("400x350")  # Increased size to fit buttons

# Create a frame
frame = ttk.Frame(root, padding=10)
frame.grid()

# Add a label for the drone status
status_label = ttk.Label(frame, text="Drone Status: Stopped", font=("Arial", 12))
status_label.grid(column=0, row=0, columnspan=3, pady=10)

# Function to move the drone
def move_drone(x, y, status_text):
    status_label.config(text=status_text)
    canvas.move(drone, x, y)

# Create a canvas for visualizing the drone
canvas = tk.Canvas(root, width=300, height=200, bg="lightblue")
canvas.grid(column=0, row=1, columnspan=3, pady=10)

# Draw a simple drone (a circle)
drone = canvas.create_oval(140, 100, 160, 120, fill="gray")

# Add buttons for controlling the drone
btn_up = ttk.Button(frame, text="Up ⬆️", command=lambda: move_drone(0, -20, "Drone Moving Up ⬆️"))
btn_up.grid(column=1, row=2, pady=5)

btn_left = ttk.Button(frame, text="Left ⬅️", command=lambda: move_drone(-20, 0, "Drone Moving Left ⬅️"))
btn_left.grid(column=0, row=3, padx=5, pady=5)

btn_right = ttk.Button(frame, text="Right ➡️", command=lambda: move_drone(20, 0, "Drone Moving Right ➡️"))
btn_right.grid(column=2, row=3, padx=5, pady=5)

btn_down = ttk.Button(frame, text="Down ⬇️", command=lambda: move_drone(0, 20, "Drone Moving Down ⬇️"))
btn_down.grid(column=1, row=4, pady=5)

btn_stop = ttk.Button(frame, text="Stop ⛔", command=lambda: status_label.config(text="Drone Stopped ⛔"))
btn_stop.grid(column=1, row=5, pady=10)

# Run the application
root.mainloop()
