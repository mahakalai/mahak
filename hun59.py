n=int(input())
l=[int(x) for x in input().split()]
l2=[int(x) for x in input().split()]
c=[]
for i in range(len(l)):
	s=l[i]+l2[i]
	c.append(s)
print(*c)	
