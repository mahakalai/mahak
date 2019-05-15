n,k=map(int,input().split())
l=[int(x) for x in input().split()]
c=0
for i in range(0,len(l)-1):
	for j in range(i+1,len(l)):
		s=l[i]+l[j]
		if s==k:
			c=c+1
if c==0:
	print("no")
else:
	print("yes")
