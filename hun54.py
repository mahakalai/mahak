n=int(input())
l=[int(x) for x in input().split()]
l1=[]
l2=[]
for i in l:
	l1.append(i)
	m=min(l1)
	l2.append(m)
print(*l2)	
