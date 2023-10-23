class Rune():
    def __init__(self, strength: int):
        self.rune_type = None
        self.strength = strength


class Rune_Defense(Rune):
    def __init__(self, strength: int):
        super().__init__(strength)
        self.rune_type = "Defense"
        self.strength = strength
