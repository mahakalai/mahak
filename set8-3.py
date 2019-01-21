n=int(input())
l,u=map(int,input().split())
c=0
for i in range(l+1,u):
	if n==i:
		c=c+1
if c>0:
	print("yes")
else:
	print("no")
