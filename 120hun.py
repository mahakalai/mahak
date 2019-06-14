n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,len(l)):
	for j in range(i+1,len(l)):
		l1=l[j+1::]
		s=l[i]+l[j]
		if s in l1:
			c=c+1
print(c)			
