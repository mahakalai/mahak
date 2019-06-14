n=int(input())
s=str(n)
sum=0
i=len(s)-1
while n:
	rem=n%10
	sum=sum+(rem**i)
	n=n//10
	i=i-1
print(sum)	
