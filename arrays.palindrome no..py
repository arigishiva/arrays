def rev(num):
    rev1=0
    while num:
        r=num%10
        num=num//10
        rev1=rev1*10+r
    return rev1
def reverse(n,data):
    c=0
    for i in range(n):
        if data[i]==rev(data[i]):
            c+=1
    return c
n=int(input())
data=list(map(int,input().split()))
c=reverse(n,data)
print(c)
