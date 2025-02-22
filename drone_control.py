import tkinter as tk
from tkinter import ttk

# start the drone
def start_drone():
    print("Drone started!")

# stop the drone
def stop_drone():
    print("Drone stopped!")

# main window
root = tk.Tk()
root.title("Drone Control Panel")
root.geometry("300x200")

# frame
frame = ttk.Frame(root, padding=10)
frame.grid()

# Add a label
ttk.Label(frame, text="Drone Control").grid(column=0, row=0, columnspan=2)

# Add buttons for controlling the drone
btn_start = ttk.Button(frame, text="Start Drone", command=start_drone)
btn_start.grid(column=0, row=1)

btn_stop = ttk.Button(frame, text="Stop Drone", command=stop_drone)
btn_stop.grid(column=1, row=1)

# Run the app
root.mainloop()
