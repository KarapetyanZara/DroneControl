import tkinter as tk
from tkinter import ttk

# main window
root = tk.Tk()
root.title("Drone Control Panel")
root.geometry("400x300")

# frame
frame = ttk.Frame(root, padding=10)
frame.grid()

# label for the drone status
status_label = ttk.Label(frame, text="Drone Status: Stopped", font=("Arial", 12))
status_label.grid(column=0, row=0, columnspan=2, pady=10)

# start the drone (simulate movement)
def start_drone():
    status_label.config(text="Drone Status: Moving 🛸")
    canvas.move(drone, 0, -20)  # Move the drone up

# stop the drone
def stop_drone():
    status_label.config(text="Drone Status: Stopped ⛔")

# canvas (visualizing the drone)
canvas = tk.Canvas(root, width=300, height=200, bg="lightblue")
canvas.grid(column=0, row=1, columnspan=2, pady=10)

# draw a simple drone (a circle)
drone = canvas.create_oval(140, 100, 160, 120, fill="gray")

# buttons for controlling
btn_start = ttk.Button(frame, text="Start Drone", command=start_drone)
btn_start.grid(column=0, row=2, padx=10, pady=5)

btn_stop = ttk.Button(frame, text="Stop Drone", command=stop_drone)
btn_stop.grid(column=1, row=2, padx=10, pady=5)

# Run the app
root.mainloop()
