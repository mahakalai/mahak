n,q=map(int,input().split())
l=[int(x) for x in input().split()]
l1=[]
for i in range(0,q):
	l2=[int(x) for x in input().split()]
	l1.append(l2)
for i in range(0,q):
	m=l1[i][0]
	n=l1[i][1]
	l3=l[m-1:n]
	print(min(l3))
