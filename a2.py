a=25
if a==24:
    print("inside if")
elif a==25:
    print(a)
else:
    print("inside else")

b=""
if b:
    print(b)
else:
    print("pls provide value")

n=int(input())
print(n)
m=n+3
print(m)
for n in range(10):
    print(n)
print()
for n in range(2,10):
    print(n)
print()
for n in range(2,20,2):
    print(n)
print()
for n in range(20,2,-2):
    print(n)
print()

n=0
while n<10:
    print(n)
    n+=1
    if n==5:
        break
print()

n=0
while n<10:
    print(n)
    n+=1
    if n==5:
        continue
print()

import random as ran
print(ran.randint(20,50))
print()

from random import randint as ran
print(ran(20,50))
print()

from random import *
print(randint(20,50))
print()
