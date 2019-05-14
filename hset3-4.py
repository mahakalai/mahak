n,k=map(int,input().split())
l=[int(x) for x in input().split()]
i=0
c=0
while i<len(l):
	j=i+1
	while j<len(l):
		s=l[i]+l[j]
		if k==s:
			c=c+1
		j=j+1
	i=i+1
if c==0:
	print("NO")
else:
	print("YES")
