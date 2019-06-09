s=input()
l=[]
for i in range(0,len(s)):
	if i%2==0:
		m=s[i].upper()
		l.append(m)
	else:
		l.append(s[i])
for i in l:
	print(i,end="")
