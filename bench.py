current = 0
count = 0

def isPrime(num):
    #prime = False
    for i in range(2, num//2):
        if num % i == 0:
            return False
        else:
            return True

while True:
    current = current + 1
    
    if isPrime(current):
        count = count + 1
        print("[", count, "]", current)
