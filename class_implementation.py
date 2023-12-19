class Robot:    # It is a convention to capitalize the first letter of a class name.
    def __init__(self, n, c, w): # __init__ creates a Python built-in constructor
        self.name = n
        self.color = c
        self.weight = w
    def introduce_self(self):
        print("My name is " + self.name)

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

# Test code
r1.introduce_self()
r2.introduce_self()
