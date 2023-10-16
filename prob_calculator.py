import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    self.contents.extend(key for key, value in kwargs.items()
                         for _ in range(value))

  def draw(self, num_balls):
    if num_balls >= len(self.contents):
      drawn = self.contents
      self.contents = []
    else:
      drawn = random.sample(self.contents, num_balls)
      [self.contents.remove(ball) for ball in drawn if ball in self.contents]
    return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0
  for _ in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn = hat_copy.draw(num_balls_drawn)
    actual_balls = {key: drawn.count(key) for key in set(drawn)}
    is_subset = all(actual_balls.get(key, 0) >= value for key, value in expected_balls.items())
    if is_subset:
      success += 1
  return success / num_experiments
