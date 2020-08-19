def fibonacci():
    fib_list = [0, 1]
    counter = 0
    while True:
        if counter == 0:
            next_num = 0
            yield next_num
        elif counter == 1:
            next_num = 1
            yield next_num
        else:
            next_num = fib_list[-1] + fib_list[-2]
            fib_list.append(next_num)
            yield next_num
        counter += 1

generator = fibonacci()
for i in range(5):
    print(next(generator))
