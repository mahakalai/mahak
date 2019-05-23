n,k=map(int,input().split())
l1=[int(x) for x in input().split()]
c=l1.count(k)
for i in range(0,c):
	l1.remove(k)
print(*l1)
