n=int(input())
c=0
for i in range(2,n):
	if n%i==0:
		print("yes")
		c=c+1
		break
if c==0:
	print("no")
