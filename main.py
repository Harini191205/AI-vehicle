import folium
import speech_recognition as sr
import time
import webbrowser
import threading

class AutonomousVehicle:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        self.state = "stopped"
        self.direction = "straight"
        self.step = 0.0001

    def start(self):
        if self.state == "stopped":
            self.state = "moving"
            self.direction = "straight"
            print("✅ Vehicle started.")
        else:
            print("ℹ️ Vehicle already moving.")

    def stop(self):
        if self.state == "moving":
            self.state = "stopped"
            print("🛑 Vehicle stopped.")
        else:
            print("ℹ️ Vehicle already stopped.")

    def turn_left(self):
        if self.state == "moving":
            self.direction = "left"
            print("↩️ Vehicle turning left.")
        else:
            print("⚠️ Can't turn. Start the vehicle first.")

    def turn_right(self):
        if self.state == "moving":
            self.direction = "right"
            print("↪️ Vehicle turning right.")
        else:
            print("⚠️ Can't turn. Start the vehicle first.")

    def move(self):
        if self.state == "moving":
            if self.direction == "straight":
                self.lat += self.step
            elif self.direction == "left":
                self.lon -= self.step
            elif self.direction == "right":
                self.lon += self.step
            print(f"Vehicle moved {self.direction} to ({self.lat:.6f}, {self.lon:.6f})")

    def status(self):
        print(f"📍 State: {self.state}, Direction: {self.direction}, Location: ({self.lat:.6f}, {self.lon:.6f})")

def update_map(lat, lon, filename="vehicle_map.html"):
    m = folium.Map(location=[lat, lon], zoom_start=18)
    folium.Marker(location=[lat, lon], popup="Vehicle", icon=folium.Icon(color='red')).add_to(m)
    m.save(filename)
    print(f"🌍 Map updated: {filename}")

def voice_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Say command (start, stop, left, right):")
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=4)
            command = r.recognize_google(audio).lower()
            print(f"🗣️ Voice command: '{command}'")
            return command
        except Exception as e:
            print(f"⚠️ Voice recognition failed or timeout: {e}")
            return None

def keyboard_command():
    cmd = input("⌨️ Enter command (start, stop, left, right, quit): ").strip().lower()
    return cmd

def main():
    start_lat, start_lon = 40.7128, -74.0060
    vehicle = AutonomousVehicle(start_lat, start_lon)

    update_map(vehicle.lat, vehicle.lon)
    webbrowser.open("vehicle_map.html")

    while True:
        cmd = voice_command()
        if cmd is None:
            cmd = keyboard_command()
            if cmd == "quit":
                print("Exiting...")
                break

        if cmd == "start":
            vehicle.start()
        elif cmd == "stop":
            vehicle.stop()
        elif cmd == "left":
            vehicle.turn_left()
        elif cmd == "right":
            vehicle.turn_right()
        else:
            print("❌ Unknown command.")

        vehicle.move()
        vehicle.status()
        update_map(vehicle.lat, vehicle.lon)

if __name__ == "__main__":
    main()
