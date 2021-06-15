import random

class Dice():
  def __init__(self, value=None, rng=None):
    self.rng = rng or random.Random()
    if value is None:
      self.value = self.rng.randint(1, 6)
    else:
      if 1 <= value  <= 6:
        self.value = value
      else:
        raise ValueError("Can only initialize a dice with a value between 1 and 6.")
  
  def roll(self):
    self.value = self.rng.randint(1, 6)

  def __repr__(self):
    return str(self.value)
