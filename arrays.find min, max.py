def min_max(n,data):
    s,l=data[0],data[0]
    for i in data:
        if s>i:
            s=i
        if l<i:
            l=i
    return s,l
n=int(input())
data=list(map(int,input().split()))
mi,ma=min_max(n,data)
print(mi,ma)
