n,k=map(int,input().split())
l=[int(x) for x in input().split()]
c=1
while c<k:
	m=max(l)
	l.remove(m)
	c=c+1
print(max(l))	
