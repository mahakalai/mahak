n,k=map(int,input().split())
l=[int(x) for x in input().split()]
c=0
for i in range(0,len(l)):
	for j in range(i+1,len(l)):
		d=abs(l[i]-l[j])
		if d==k:
			c=c+1
print(c)			
