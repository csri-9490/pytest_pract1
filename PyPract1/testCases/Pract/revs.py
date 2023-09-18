class ReverseIterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = len(sequence)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.sequence[self.index]
        else:
            raise StopIteration()

# Test the ReverseIterator class
numbers = [1, 2, 3, 4, 5]
reverse_iter = ReverseIterator(numbers)

for num in reverse_iter:
    print(num)
