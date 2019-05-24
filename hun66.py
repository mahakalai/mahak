n=int(input())
l=[int(x) for x in input().split()]
p=int(input())
p1=str(p)
c=0
for i in range(0,len(l)):
	m=l[i]
	s=str(m)
	m1=s[:2]
	if m1==p1:
		c=c+1
print(c)		
