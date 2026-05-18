from collections import defaultdict

class FreqStack:

    def __init__(self):
        # Stores frequency of each value
        self.freq = defaultdict(int)

        # Maps frequency -> stack of values having that frequency
        self.group = defaultdict(list)

        # Current maximum frequency
        self.max_freq = 0

    def push(self, val: int) -> None:
        # Increase frequency of val
        self.freq[val] += 1
        f = self.freq[val]

        # Update maximum frequency
        if f > self.max_freq:
            self.max_freq = f

        # Add value to the stack corresponding to its frequency
        self.group[f].append(val)

    def pop(self) -> int:
        # Pop the most recent element with highest frequency
        val = self.group[self.max_freq].pop()

        # Decrease its frequency
        self.freq[val] -= 1

        # If no more elements at this frequency, decrease max_freq
        if not self.group[self.max_freq]:
            self.max_freq -= 1

        return val