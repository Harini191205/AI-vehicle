class AutonomousVehicle:
    def __init__(self):
        self.state = "stopped"
        self.direction = "straight"

    def start(self):
        if self.state == "stopped":
            self.state = "moving"
            self.direction = "straight"
            print("✅ Vehicle started. Moving forward.")
        else:
            print("ℹ️ Vehicle is already moving.")

    def stop(self):
        if self.state == "moving":
            self.state = "stopped"
            print("🛑 Vehicle stopped.")
        else:
            print("ℹ️ Vehicle is already stopped.")

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

    def status(self):
        print(f"📍 STATUS: State = {self.state}, Direction = {self.direction}")


def ai_decision_system(command, vehicle):
    print(f"\n🔘 AI Command Received: '{command}'")

    if command == "start":
        vehicle.start()
    elif command == "stop":
        vehicle.stop()
    elif command == "left":
        vehicle.turn_left()
    elif command == "right":
        vehicle.turn_right()
    else:
        print("❌ Unknown command.")

    vehicle.status()


if __name__ == "__main__":
    vehicle = AutonomousVehicle()

    # Simulated AI Command Inputs
    command_list = ["start", "left", "right", "stop", "left", "start", "right", "stop"]

    print("🚗 Starting Autonomous Vehicle AI Controller...\n")

    for cmd in command_list:
        ai_decision_system(cmd, vehicle)

    print("\n✅ Program completed.")
