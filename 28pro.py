n=int(input())
l=[int(x) for x in input().split()]
l1=sorted(l)
c=0
s=0
for i in range(0,len(l)):
	if l1[i]>=s:
		c=c+1
	s=s+l1[i]	
print(c)		
