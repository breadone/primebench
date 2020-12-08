import time
import numpy as np

def isPrime(num): #works perfectly except for the number 4!!!
    if num > 1:
        for i in range(2, num//2):
            if num % i == 0:
                return False
                break
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
    starttime = time.time()
    while count < limit:
        current = current + 1    
        if isPrime(current):
            count = count + 1
            print("[",count,"]", current)
    elapsedTime = time.time() - starttime
    print("Time Elapsed:", elapsedTime, "seconds")

def milebench(max):
    current = 0
    count = 0

    sTime = time.time()
    eTime = sTime
    while True:
        current = current + 1    
        if isPrime(current):
            count = count + 1
            aTime = round((time.time() - sTime) - eTime, 2)
            eTime = round(time.time() - sTime, 2)
            if count % 1000 == 0:
                print("[",count,"]", current, "[", eTime, "s |", aTime, "s]")


print("select function:\n1. free run\n2. run for 5 mins\n3. run for custom amount\n4. run until 10,000\n5. run until custom amount\n6. milestone bench")
inp = input("choice: ")

if inp == "1":
    bench()
if inp == "2":
    timedbench(5)
if inp == "3":
    t = int(input("enter time in minutes: "))
    timedbench(t)
if inp == "4":
    limitbench(10000)
if inp == "5":
    l = int(input("enter a limit: "))
    limitbench(l)
if inp == "6":
    milebench(50000)
if inp == "testnum":
    test = int(input("what number would you like to test: "))
    print(isPrime(test))
