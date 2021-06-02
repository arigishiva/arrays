import math as m
def isprime(num):
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            return 0
        return 1
def countprime(n,data):
    pc=0
    for i in data:
        if isprime(i):
            pc+=1
    return pc
n=int(input())
data=list(map(int,input().split()))
pc=countprime(n,data)
print(pc)
