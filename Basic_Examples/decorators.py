def inspect(func):
    def wrapped_func(*args, **kwargs):
        print(f"Running {func.__name__}")
        val = func(*args, **kwargs)
    return wrapped_func

# If we call inspect, we get a function as a returned value.


@inspect
def combine(a, b):
    return a+b


combine(1, 2)
