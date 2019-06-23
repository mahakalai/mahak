n=int(input())
l=list(map(int,input().split()))
l1=[1]*n
for i in range(n):
    if i==0:
        if l[i]>l[i+1]:
            l1[i]=l1[i]+l1[i+1]
    elif i>0:
        if l[i]>l[i-1]:
            l1[i]=l1[i]+l1[i-1]
print(sum(l1))
