n=int(input())
l=[int(x) for x in input().split()]
s1=0
s2=0
for i in range(0,len(l)):
	if i%2==0:
		s1=s1+l[i]
	else:
		s2=s2+l[i]
if s1>s2:
	print(s1)
else:
	print(s2)
  
