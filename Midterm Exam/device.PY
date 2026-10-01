class Device:
    room = "Lab 01"          # class attribute, shared by all instances

    def __init__(self, name):
        self.name = name


first = Device("D-01")
second = Device("D-02")

print(first.room)    # Lab 01
print(second.room)   # Lab 01

# Change the class attribute: affects every instance that hasn't overridden it
Device.room = "Lab 2"
print(first.room)    # Lab 2
print(second.room)   # Lab 2

# Set room on one instance: creates an instance attribute that shadows the class one
first.room = "Repair Bench"
print(first.room)    # Repair Bench
print(second.room)   # Lab 2
print(Device.room)   # Lab 2