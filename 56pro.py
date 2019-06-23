m,k=map(int,input().split())
l=list(map(int,input().split()))
d=0
for i in l:
	d=abs(i-d)
if d<=m:
	print(d)
else:	
	print(abs(86400-d))
