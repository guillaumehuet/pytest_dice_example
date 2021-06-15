import pytest

@pytest.mark.parametrize('n', range(1, 7))
def test_dice_deterministic(n):
  from context import dice
  d = dice.Dice(n)
  assert str(d) == str(n)

@pytest.mark.parametrize('n', [-42, -1, 0, 7, 42])
def test_dice_not_valid(n):
  from context import dice
  with pytest.raises(ValueError):
    dice.Dice(n)

def test_dice_seeded():
  from context import dice
  import random
  random.seed(0)
  expected = tuple(random.randint(1, 6) for _ in range(10))
  random.seed(0)
  d = dice.Dice()
  for e in expected:
    assert(str(d) == str(e))
    d.roll()
