n=int(input())
l=[]
n1=1
for i in range(1,n+1):
	if i==1:
		print("1")
	else:
		n1=n1+2
		n2=n1
		while n2:
			l.append("1")
			n2=n2-1
		print(*l)	
	l=[]	
