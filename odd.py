n,Q=map(int,input().split( ))
l=[int(a) for a in range(n+1,Q)]
a=0
for i in range(n+1,Q):
	if l[a]%2==1:
		print(l[a],end=" ")
	a=a+1
