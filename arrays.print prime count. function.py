import math as m
def isprime(num):
    if num==1:
        return 0
    
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            return 0
        return 1
def findprime(n,data):
     prime=[]
     nonprime=[]
     for i in data:
         if isprime(i):
            prime.append(i)
         else:
            nonprime.append(i)
     return prime,nonprime
n=int(input())
data=list(map(int,input().split()))
prime,np=findprime(n,data)
print(*prime)
print(*nonprime)
