import tkinter as tk
from dronekit import connect, VehicleMode

class DroneControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drone Control Panel")
        
        # Connection String
        self.conn_label = tk.Label(root, text="Connection String:")
        self.conn_label.grid(row=0, column=0)
        self.conn_entry = tk.Entry(root)
        self.conn_entry.insert(0, "/dev/ttyUSB0")
        self.conn_entry.grid(row=0, column=1)
        
        self.baud_label = tk.Label(root, text="Baud Rate:")
        self.baud_label.grid(row=0, column=2)
        self.baud_entry = tk.Entry(root)
        self.baud_entry.insert(0, "57600")
        self.baud_entry.grid(row=0, column=3)
        
        self.connect_button = tk.Button(root, text="Connect", command=self.connect_drone)
        self.connect_button.grid(row=0, column=4)
        
        self.disconnect_button = tk.Button(root, text="Disconnect", command=self.disconnect_drone)
        self.disconnect_button.grid(row=0, column=5)
        
        self.status_label = tk.Label(root, text="Status: Not Connected", fg="red")
        self.status_label.grid(row=1, columnspan=6)
        
        # Control buttons
        self.arm_button = tk.Button(root, text="Arm", command=self.arm_drone)
        self.arm_button.grid(row=2, column=0)
        
        self.disarm_button = tk.Button(root, text="Disarm", command=self.disarm_drone)
        self.disarm_button.grid(row=2, column=1)
        
        self.takeoff_button = tk.Button(root, text="Takeoff", command=self.takeoff)
        self.takeoff_button.grid(row=2, column=2)
        
        self.return_button = tk.Button(root, text="Return to Launch", command=self.return_to_launch)
        self.return_button.grid(row=2, column=3)
        
        self.land_button = tk.Button(root, text="Land", command=self.land)
        self.land_button.grid(row=2, column=4)
        
        self.loiter_button = tk.Button(root, text="Loiter", command=self.set_loiter_mode)
        self.loiter_button.grid(row=2, column=5)
        
        self.altitude_label = tk.Label(root, text="Altitude: 0m")
        self.altitude_label.grid(row=3, columnspan=6)
        
        self.longitude_label = tk.Label(root, text="Longitude: 0")
        self.longitude_label.grid(row=4, columnspan=6)
        
        self.latitude_label = tk.Label(root, text="Latitude: 0")
        self.latitude_label.grid(row=5, columnspan=6)
        
        self.vehicle = None
    
    def connect_drone(self):
        conn_str = self.conn_entry.get()
        baud_rate = self.baud_entry.get()
        try:
            self.vehicle = connect(conn_str, baud=int(baud_rate), wait_ready=True)
            self.status_label.config(text="Connected", fg="green")
            self.update_telemetry()
        except Exception as e:
            self.status_label.config(text=f"Connection Failed: {e}", fg="red")
    
    def disconnect_drone(self):
        if self.vehicle:
            self.vehicle.close()
            self.vehicle = None
            self.status_label.config(text="Disconnected", fg="red")
    
    def arm_drone(self):
        if self.vehicle:
            self.vehicle.armed = True
    
    def disarm_drone(self):
        if self.vehicle:
            self.vehicle.armed = False
    
    def takeoff(self):
        if self.vehicle and self.vehicle.armed:
            self.vehicle.mode = VehicleMode("GUIDED")
            self.vehicle.simple_takeoff(5)  # 5 meters altitude
    
    def return_to_launch(self):
        if self.vehicle:
            self.vehicle.mode = VehicleMode("RTL")
    
    def land(self):
        if self.vehicle:
            self.vehicle.mode = VehicleMode("LAND")
    
    def set_loiter_mode(self):
        if self.vehicle:
            self.vehicle.mode = VehicleMode("LOITER")
    
    def update_telemetry(self):
        if self.vehicle:
            self.altitude_label.config(text=f"Altitude: {self.vehicle.location.global_relative_frame.alt:.2f}m")
            self.longitude_label.config(text=f"Longitude: {self.vehicle.location.global_frame.lon:.6f}")
            self.latitude_label.config(text=f"Latitude: {self.vehicle.location.global_frame.lat:.6f}")
            self.root.after(1000, self.update_telemetry)  # Update every second

if __name__ == "__main__":
    root = tk.Tk()
    app = DroneControlApp(root)
    root.mainloop()
