class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def add_points(self, points):
        self.score += points

    def __repr__(self):
        return f"Player(name={self.name!r}, score={self.score})"


ana = Player("Ana", 10)
ben = Player("Ben")      # score defaults to 0

print(ana)  # Player(name='Ana', score=10)
print(ben)  # Player(name='Ben', score=0)

ana.add_points(5)
ben.add_points(7)

print(ana)  # Player(name='Ana', score=15)
print(ben)  # Player(name='Ben', score=7)