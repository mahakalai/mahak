s=input()
l=list(s)
l1=[]
s1=""
for i in l:
	if l.count(i)==1:
		l1.append(i)
s1=s1.join(l1)
print(s1)
