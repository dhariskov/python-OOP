import random
def solution():
    def integers():
        counter = 1
        while True:
            yield counter
            counter += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        ll = []
        for i in seq:
            ll.append(i)
            if len(ll) == n:
                return ll

    return (take, halves, integers)


take = solution()[0]
print(take)
halves = solution()[1]
print(halves)
print(take(5, halves()))
