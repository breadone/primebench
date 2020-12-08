import time

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

def timedbench(tEnd):
    t = time.time() + (60 * tEnd)    
    current = 0
    count = 0
    
    while time.time() < t:
        current = current + 1    
        if isPrime(current):
            count = count + 1
            print("[",count,"]", current)

print("select function:\n1. free run\n2. run for 5 mins\n3. run for custom amount\n4. run until 10 million")
inp = input("choice: ")

if inp == "1":
    bench()
if inp == "2":
    timedbench(5)
if inp == "3":
    t = int(input("enter time in minutes: "))
    timedbench(t)

