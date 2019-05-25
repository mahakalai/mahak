n=int(input())
sum=0
s=str(n)
l=len(s)
while n>0:
	rem=n%10
	sq=rem**l
	sum=sum+sq
	n=n//10
print(sum)	
