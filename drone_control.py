import tkinter as tk
from tkinter import ttk

# Main window
root = tk.Tk()
root.title("Drone Control Panel")
root.geometry("300x200")

# Frame
frame = ttk.Frame(root, padding=10)
frame.grid()
# Label
ttk.Label(frame, text="Drone Control").grid(column=0, row=0, columnspan=2)

# Buttons
btn_start = ttk.Button(frame, text="Start Drone")
btn_start.grid(column=0, row=1)

btn_stop = ttk.Button(frame, text="Stop Drone")
btn_stop.grid(column=1, row=1)

# Run the application
root.mainloop()
