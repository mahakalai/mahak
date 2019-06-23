s=input()
l=[]
s1=""
for i in range(len(s)-1):
	if s[i]==" " and s[i+1]==" ":
		continue
	else:
		l.append(s[i])
l.append(s[-1])
s1=s1.join(l)
print(s1)
