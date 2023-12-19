class Goblin:
    def __init__(self, n, c, w):
        self.name = n
        self.color = c
        self.weight = w
    def introduce_self(self):
        print("I am " + self.name)
class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i
    def sit_down(self):
        self.is_sitting = True
    def stand_up(self):
        self.is_sitting = False

def exchange_goblins():
    p1.goblin_owned = g2
    p2.goblin_owned = g1
def look_at_owner():
    g1.looking_at = p1
    g2.looking_at = p2

g1 = Goblin("Goblins No.1", "red", 30)
g2 = Goblin("Goblins No.2", "blue", 40)
g1.looking_at = g2
g2.looking_at = g1

p1 = Person("ParPar", "sooty", False)
p2 = Person("LyuLyu", "gummy", True)
p1.goblin_owned = g1 # p1 owns g1
p2.goblin_owned = g2 # p2 owns g2

p1.goblin_owned.introduce_self()
