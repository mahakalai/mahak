s=input()
l=list(s)
l1=l[::-1]
s1=""
if l==l1:
	l.remove(l[-1])
	l2=l[::-1]
	s1=s1.join(l2)
	print(s1)
else:
	print(s)
	
