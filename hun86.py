n=int(input())
c=0
for i in range(1,n+1):
	s=str(i)
	if "2" in s:
		co=s.count("2")
		c=c+co
print(c)		
