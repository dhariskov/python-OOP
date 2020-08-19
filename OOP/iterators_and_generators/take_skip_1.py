class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.result = -step

    def __iter__(self):
        return self

    def __next__(self):
        if not self.count <= 0:
            self.count -= 1
            self.result += self.step
            return self.result

        else:
            raise StopIteration()

numbers = take_skip(2, 6)
for number in numbers:
    print(number)
