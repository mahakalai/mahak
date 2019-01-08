n,Q=map(int,input().split( ))
l=[int(a) for a in range(n+1,Q) if a%2==0]
for i in range(0,len(l)-1):
      print(l[i],end=" ")
print(l[-1])   
