def isPrime(num):
    for i in range(2, num//2):
        if num % i == 0:
            return False
        else:
            return True

def bench(): 
    current = 0
    count = 0

    while True:
        current = current + 1    
        if isPrime(current):
            count = count + 1
            print("[",count,"]", current)

bench()

