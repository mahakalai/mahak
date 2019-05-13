n,m=map(int,input().split())
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
c=0
for i in range(0,len(b)):
	if b[i] in a:
		c=c+1
if c==len(b):
	print("YES")
else:
	print("NO")
