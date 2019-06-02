s=input()
l=[]
for i in s:
	c=s.count(i)
	if c==1 and i not in l and i!=" ":
		l.append(i)
print(*l)		
