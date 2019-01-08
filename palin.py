n=n1=int(input())
sum=0
while n>0:
    rem=n%10
    sum=(sum*10)+rem
    n=n//10
if n1==sum:
	print("yes")
else:
	print("no")
   
    
