n1=n=int(input())
sum=0
while n>0:
   rem=n%10
   cube=rem*rem*rem
   sum=sum+cube
   n=n//10
if n1==sum:
  print("yes")
else:
  print("no")
  
   
