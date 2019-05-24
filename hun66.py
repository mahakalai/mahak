n=int(input())
l=[x for x in input().split()]
p=input()
c=0
for i in range(0,len(l)):
	s=l[i]
	m1=s[:2]
	if m1==p:
		c=c+1
print(c)		
