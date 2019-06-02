n=int(input())
l=[int(x) for x in input().split()]
c=0
for i in range(0,len(l)-1):
	for j in range(i+1,len(l)):
		if l[i]<l[j]:
			c=c+1
print(c)			
