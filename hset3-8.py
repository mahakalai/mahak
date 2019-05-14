s=input()
l=list(s)
l1=[]
s=""
for i in range(0,len(l)):
	if l[i] not in l1:
		l1.append(l[i])
s=s.join(l1)
print(s)
