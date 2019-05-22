n,k=map(int,input().split())
l=[int(x) for x in input().split()]
for i in range(0,k):
	l.append(l[0])
	l.remove(l[0])
print(*l)	
