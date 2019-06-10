s=input()
l1=[]
if "." in s:
	s1=s.replace(".","")
l=s1.split(" ")	
for i in range(0,len(l)):
	if i%2==0:
		m=str(l[i])
		m1=m[::-1]
		l1.append(m1)
	else:
		l1.append(l[i])
	l1.append(" ")
for i in range(0,len(l1)-1):
	print(l1[i],end="")
