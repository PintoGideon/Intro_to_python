

def fibonacci(limit):

    current = 0
    next = 1

    while current < limit:
        current, next = next, next+current
        yield current


for n in fibonacci(10):
    print(n, end=',')
