n=int(input())
l=[]
for i in range(n):
	l1=[int(x) for x in input().split()]
	m=sum(l1)
	l.append(m)
print(sum(l)/(n*n))	
