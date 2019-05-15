k=int(input())
x=[]
for i in range(0,k):
	l=[int(x) for x in input().split()]
	for i in l:
		x.append(i)
l1=sorted(x)
print(*l1)
