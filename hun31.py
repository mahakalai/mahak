n=int(input())
l=[int(x) for x in input().split()]
l1=[]
mul=1
for i in range(1,len(l)):
   mul=mul*l[i]
   l1.append(mul)  
print(max(l1))   
