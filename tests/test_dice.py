import pytest
import random
import statistics

@pytest.mark.parametrize('n', range(1, 7))
def test_dice_init_deterministic(n):
  import dice
  d = dice.Dice(n)
  assert d.value == n

@pytest.mark.parametrize('n', [-42, -1, 0, 7, 42])
def test_dice_init_invalid(n):
  import dice
  with pytest.raises(ValueError):
    dice.Dice(n)

def test_dice_init_rng():
  import dice
  n = random.Random(0).randint(1, 6)
  d = dice.Dice(rng = random.Random(0))
  assert d.value == n

@pytest.mark.parametrize('n', range(1, 7))
def test_dice_repr(n):
  import dice
  d = dice.Dice()
  d.value = n
  assert str(d) == str(n)

def test_dice_fairness():
  import dice
  results = []
  d = dice.Dice(rng = random.Random(42))
  for _ in range(10_000):
    results.append(d.value)
    d.roll()
  assert min(results) >= 1
  assert max(results) <= 6
  assert 6 < statistics.mean(results)*2 < 8          # perfect dice mean is 7/2
  assert 104 < statistics.variance(results)*36 < 106 # perfect dice variance is 105/36
