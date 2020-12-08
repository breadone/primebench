current = 0
count = 0

def isPrime(num):
    #prime = False
    for i in range(2, int(num/2)):
        if num % i == 0:
            return True
        else:
            return False

while True:
    current = current + 1
    
    if isPrime(current):
        count = count + 1
        print("[{0}] {1}", count, current)
