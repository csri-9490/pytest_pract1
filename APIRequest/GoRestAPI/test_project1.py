import random


class Testone:
    def test_roll(self):
        min_value=1
        max_value=6
        roll=random.randint(min_value,max_value)
        return roll

value=Testone()
print(value.test_roll())