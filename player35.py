s=input()
l=[]
for i in s:
	c=s.count(i)
	if c==1 and i not in l and i!=" ":
		m=i.lower()
		l.append(m)
print(*l)		
