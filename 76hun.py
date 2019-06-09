n=int(input())
l=[]
for i in range(n):
	l1=[int(x) for x in input().split()]
	m=sum(l1)
	l.append(m)
m=sum(l)/(n*n)
print("%.6f" %m)	
