class Device:
    room = "Lab 01"         

    def __init__(self, name):
        self.name = name


first = Device("D-01")
second = Device("D-02")

print(first.room)    # Lab 01
print(second.room)   # Lab 01


Device.room = "Lab 2"
print(first.room)    # Lab 2
print(second.room)   # Lab 2


first.room = "Repair Bench"
print(first.room)    # Repair Bench
print(second.room)   # Lab 2
print(Device.room)   # Lab 2
