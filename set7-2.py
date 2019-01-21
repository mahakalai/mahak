s=input()
n=int(s)
c=0
while n:
	rem=n%10
	if rem==0 or rem==1:
		d=0
	else:
		c=c+1
	n=n//10
if c>0:
	print("no")
else:
	print("yes")
