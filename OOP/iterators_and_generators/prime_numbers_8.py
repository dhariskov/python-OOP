def get_primes(ll):
    for num in ll:
        counter = 0
        for dev in range(1, num +1):
            if num % dev == 0:
                counter += 1
                if counter > 2:
                    break
        if counter == 2:
            yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

