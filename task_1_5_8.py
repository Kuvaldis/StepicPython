class MoneyBox:
    def __init__(self, capacity):
        self.coins = 0
        self.capacity = capacity

    def can_add(self, v):
        return self.coins + v <= self.capacity

    def add(self, v):
        self.coins += v
