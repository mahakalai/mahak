n=int(input())
sum=0
while n>0:
	rem=n%10
	for i in range(1,rem+1):
		sum=sum+i
	n=n//10
print(sum)	
