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

def limitbench(limit):
    current = 0
    count = 0

    while current < limit:
        current = current + 1    
        if isPrime(current):
            count = count + 1
            print("[",count,"]", current)
    #TODO: make timer

print("select function:\n1. free run\n2. run for 5 mins\n3. run for custom amount\n4. run until 10 million\n5. run until custom amount")
inp = input("choice: ")

if inp == "1":
    bench()
if inp == "2":
    timedbench(5)
if inp == "3":
    t = int(input("enter time in minutes: "))
    timedbench(t)
if inp == "4":
    limitbench(10000000)
if inp == "5":
    l = input("enter a limit: ")
    limitbench(l)

