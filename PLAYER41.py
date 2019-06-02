n,k=map(int,input().split())
while n>k:
	n=n//k
if n==k:
	print("yes")
else:
	print("no")
