class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        log_str = f"Function {self.func.__name__} was add called. Result: {self.func(*args, **kwargs)}\n"
        with open('results.txt', 'a') as open_file:
            open_file.write(log_str)


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)
