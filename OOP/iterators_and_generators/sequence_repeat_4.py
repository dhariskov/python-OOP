class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.temp_sequence = self.sequence
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not len(self.temp_sequence) > self.number:
            self.temp_sequence += self.sequence
            return self.__next__()
        if self.number > self.counter:
            self.counter += 1
            result = self.temp_sequence[0]
            self.temp_sequence = self.temp_sequence[1::]
            return result
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
