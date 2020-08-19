class dictionary_iter:
    def __init__(self, dictionary:dict):
        self.dictionary = dictionary

    def __iter__(self):
        return self

    def __next__(self):
        while self.dictionary:
            k = next(iter(self.dictionary))
            v = self.dictionary[k]
            self.dictionary.pop(k)
            return k, v
        else:
            raise StopIteration()

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
