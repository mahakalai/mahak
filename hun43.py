n1=int(input())
l1=[int(X) for X in input().split()]
c=0
for i in range(1,n1+1):
    if n1*i in l1:
        c=c+1
print(c)        
