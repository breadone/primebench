count = 0
current = 2

def f(current):
    for i in range(current):
        current = current + i

    print(count, f(current))


while True:
    f(2)